from app import db
from models import Druginfo, DrugItem, Client, Pharmacy, Order
from datetime import datetime, timedelta
from time import time

def db_clear():
    two_days = timedelta(days=2)
    current_time = datetime.utcnow()
    expiration_time = current_time - two_days
    orders_expired = Order.query.filter(Order.date_ordered <= expiration_time).all()
    print(orders_expired)
    for order in orders_expired:
        db.session.delete(order)
        db.session.commit()
    print(orders_expired)