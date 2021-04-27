from flask import render_template
from medivisor import db, mail
from medivisor.models import Druginfo, DrugItem, Client, Pharmacy, Order
from datetime import datetime, timedelta
from time import time
from flask_mail import Message


def send_confirmation(email, order_id):
    order = Order.query.filter(Order.id == order_id).first()
    msg = Message('Potwierdzenie dokonania rezerwacji', sender="Medivisor", recipients=[email])
    msg.html = render_template("confirmation-mail.html", order=order)
    mail.send(msg)


def db_confirm():
    unconfirmed_orders = Order.query.filter(Order.confirmation_send == 0).all()
    for order in unconfirmed_orders:
        client = Client.query.filter(Client.id == order.client_id).first()
        email = client.email
        send_confirmation(email, order.id)
        order.confirmation_send = 1
        db.session.commit()

def send_annulation(email, order_id):
    order = Order.query.filter(Order.id == order_id).first()
    msg = Message(
        "Anulacja rezerwacji", sender="natalka_nowak@tlen.pl ", recipients=[email]
    )
    msg.html = render_template("annulation-mail.html", order=order)
    mail.send(msg)

def increase_quantity(drugitem_id, quantity):
    drugitem = DrugItem.query.filter(DrugItem.id == drugitem_id).first()
    old_quantity = drugitem.quantity
    new_quantity = old_quantity + quantity
    drugitem.quantity = new_quantity
    db.session.commit()


def db_clear():
    two_days = timedelta(days=2)
    current_time = datetime.utcnow()
    expiration_time = current_time # - two_days
    orders_expired = Order.query.filter(Order.date_ordered <= expiration_time).filter(Order.expired == False).all()
    for order in orders_expired:
        client = Client.query.filter(Client.id == order.client_id).first()
        email = client.email
        send_annulation(email, order.id)
        order.expired = 1
        db.session.commit()
        # increase drug quantity in drug_item table:
        for item in order.orders_items:
            increase_quantity(item.drugitem_id, item.quantity)