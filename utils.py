from app import db, mail
from models import Druginfo, DrugItem, Client, Pharmacy, Order
from datetime import datetime, timedelta
from time import time
from flask_mail import Message

def send_annulation(email):
    msg = Message('Anulowano rezerwację', sender='natalka_nowak@tlen.pl ', recipients=[email])
    msg.body = f''' Twoja rezerwacja leków została anulowana '''
    mail.send(msg)

def db_clear():
    two_days = timedelta(days=2)
    current_time = datetime.utcnow()
    expiration_time = current_time - two_days
    orders_expired = Order.query.filter(Order.date_ordered <= expiration_time).all()
    for order in orders_expired:
        client = Client.query.filter(Client.id == order.client_id).first()
        email = client.email
        send_annulation(email)
        db.session.delete(order)
        db.session.commit()
        # increase drug quantity in drug_item table:
        drugitem = DrugItem.query.filter(DrugItem.id == order.drugitem_id).first()
        old_quantity = drugitem.quantity
        new_quantity = old_quantity + order.quantity
        drugitem.quantity = new_quantity
        db.session.commit()

