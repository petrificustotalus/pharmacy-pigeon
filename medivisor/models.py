from datetime import datetime
from sqlalchemy import *
from datetime import datetime
from time import time

from medivisor import db


class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    phone = db.Column(db.Integer)
    # that will be new separate table:
    adress = db.Column(db.String(140))
    open_hours = db.Column(db.String(140))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Pharmacy id: {self.id}, name: {self.name}, phone: {self.phone}, adress: {self.adress}>"

class Druginfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    size = db.Column(db.Integer)
    form = db.Column(db.String)
    power = db.Column(db.Float)
    unit = db.Column(db.String)
    prescription = db.Column(db.Boolean)
    refundation = db.Column(db.Integer)
    drugitems = db.relationship(
        "DrugItem", backref=db.backref("druginfo", lazy="joined")
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Drug id: {self.id}, name: {self.name}, size: {self.size}, power: {self.power}, prescription: {self.prescription}, refundation: {self.refundation}>"


class DrugItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    druginfo_id = db.Column(db.Integer, db.ForeignKey("druginfo.id"))
    pharmacy_id = db.Column(db.Integer, db.ForeignKey("pharmacy.id"))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    order_items = db.relationship("OrderItem", backref="drugitem", lazy=True)
    pharmacies = db.relationship(
        "Pharmacy", backref=db.backref("drug_item", lazy="joined")
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<DrugItem id: {self.id}, druginfo id: {self.druginfo_id}, pharmacy id: {self.pharmacy_id}, price: {self.price}, quantity: {self.quantity}>"


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))  # not null
    surname = db.Column(db.String(140))  # not null
    email = db.Column(db.String(140))  # not null
    phone = db.Column(db.Integer)
    address = db.Column(db.String(140))  # not null if delivery
    orders = db.relationship("Order", backref="client", lazy=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Pharmacy id: {self.id}, name: {self.name}, surname: {self.surname}, email: {self.adress}, phone: {self.phone}, address: {self.address}>"


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drugitem_id = db.Column(db.Integer, db.ForeignKey("drug_item.id"), nullable=False)
    quantity = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    drug_item = db.relationship("DrugItem", backref="orderitem", lazy=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<OrderItem id: {self.id}, drugitem id: {self.drugitem_id}, quantity: {self.quantity}, order id: {self.order_id}>"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    date_ordered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    confirmation_send = db.Column(db.Boolean, nullable=False, default=0)
    expired = db.Column(db.Boolean, nullable=False, default=0)
    # orders_ids one to many relationship
    orders_items = db.relationship(
        "OrderItem", backref=db.backref("order", lazy="joined")
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Order id: {self.id}, client_id: {self.client_id}, date ordered: {self.date_ordered}, confirmation send: {self.confirmation_send}, expired: {self.expired}, orders items: {self.orders_items}>"
        