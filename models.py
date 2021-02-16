from datetime import datetime
from sqlalchemy import *
from datetime import datetime
from time import time

from app import db


# none of them can be null
# dodać miasto
class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    phone = db.Column(db.Integer)
    # that will be new separate table:
    adress = db.Column(db.String(140))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Pharmacy id: {self.id}, name: {self.name}, phone: {self.phone}, adress: {self.adress}>"


# należy zmienić nazwy 'adress' na 'address'
# power na 'ilość_czynnika_aktywnego' ang
# state i refundation powinny być SELECT
# none of them can be null
class Druginfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    size = db.Column(db.Integer)
    power = db.Column(db.Float)
    state = db.Column(db.String(140))
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
    orders = db.relationship("Order", backref="drugitem", lazy=True)

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


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"),  nullable=False)
    drugitem_id = db.Column(db.Integer, db.ForeignKey("drug_item.id"), nullable=False)
    date_ordered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return (
            f"<Order id: {self.id}, client_id: {self.client_id}, drugitem_id: {self.drugitem_id}, date_ordered: {self.date_ordered}>"
        )


# dla 100 leków: +
# -nazwa leku +
# -wielkość opakowania  [oddzielna tabela] +
# -cena dla każdej z aptek +
# -ilość opakowań w każdej aptece +
# -moc leku (mlg/ml) +
# - postać leku +
# -czy na recepte +
# refundacja (-; 25%, 50%, 75%) [opisać logikę refundacji] +

# dla 3 aptek:
# -nazwa apteki +
# -nr telefonu +
# -adres (geolokalizacjia) +

# dla zamówień/rezerwacji:
# imię nazwisko klienta +
# nr telefonu (opcjonalnie) +
# adres e-mail +
# adres klienta (jeśli zamawia z dostawą) +
# data/godzina złożenia zamówienia +
# nazwa zamawianego leku +
# nazwa apteki w której zamówiono lek +
# opłacono=tak/nie
# recepta=tak/nie
# refundacja
# cena zamówienia [zł]

# ilość leku dostępna w aptece +