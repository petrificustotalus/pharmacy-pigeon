from app import db, mail, scheduler
from models import Druginfo, DrugItem, Client, Pharmacy, Order
from datetime import datetime, timedelta
from time import time
from flask_mail import Message

# reservation_annulation_scheduler przeniosłam z app.py jak próbowałam ogarnąć zapentlone importy 

def reservation_annulation_scheduler():
    scheduler.add_job(id='Scheduled task', func = db_clear, trigger = 'interval', seconds = 60)
    scheduler.start()

def send_annulation(email):
    msg = Message('Anulowano rezerwację', sender='natalka_nowak@tlen.pl ', recipients=[email])
    msg.body = f''' Twoja rezerwacja leków została anulowana '''
    mail.send(msg)

def db_clear():
    two_days = timedelta(days=2)
    current_time = datetime.utcnow()
    # expiration_time = current_time - two_days
    expiration_time = current_time
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
    print("db_clear done")

