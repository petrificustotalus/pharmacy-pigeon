from sqlalchemy import *
from datetime import datetime
from time import time

from app import db

# none of them can be null
class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    phone = db.Column(db.Integer)
    # that will be new separate table:
    adress = db.Column(db.String(140))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return f'<Pharmacy id: {self.id}, name: {self.name}, phone: {self.phone}, adress: {self.adress}>'


# należy zmienić nazwy 'adress' na 'address'
# power na 'ilość_czynnika_aktywnego' ang
# state i refundation powinny być SELECT
# none of them can be null
class Drug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    size = db.Column(db.Integer)
    power = db.Column(db.Float)
    state = db.Column(db.String(140))
    prescription = db.Column(db.Boolean)
    refundation = db.Column(db.Integer)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 

    def __repr__(self):
        return f'<Drug id: {self.id}, name: {self.name}, size: {self.size}, power: {self.power}, prescription: {self.prescription}, refundation: {self.refundation}>'

# PRICES TABLE:
# Is it supposed to be one table like this: (OPTION 1)
prices = db.Table('prices',
                    db.Column('drug_id', db.Integer, db.ForeignKey('drug.id'))
                    db.Column('pharmacy_id', db.Integer, db.ForeignKey('pharmacy.id'))
                    db.Column('price', db.Integer)
                    db.Column('quantity_available', db.Integer)
# 
# Or is it better to do 3 columns with prices for each one from the 3 pharmacies (and then I have no idea how to conect the column with the corect pharmacy, but i gues it would be easier :P)?
# Or for each pharmacy make table with: drug_id, drug_price, available_quantity? 

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))    # not null
    surname = db.Column(db.String(140))  # not null
    email = db.Column(db.String(140))  # not null
    phone = db.Column(db.Integer)
    address = db.Column(db.String(140))  # not null if delivery


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 

    def __repr__(self):
        return f'<Pharmacy id: {self.id}, name: {self.name}, surname: {self.surname}, email: {self.adress}, phone: {self.phone}, address: {self.address}>'

# # not inicialized yet - not sure at all how it should working :/
# order = db.Table('order',
#                     db.Column('order_id', db.Integer, primary_key=True),
#                     db.Column('client_id', db.Integer, db.ForeignKey('client.id')),
#                     db.Column('pharmacy_id', db.Integer, db.ForeignKey('pharmacy.id')),
#                     db.Column('drug_id', db.Integer, 'pharmacy.id'))
#                     # AJAJAJAJAJAJAJ


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
# -nazwa apteki
# -nr telefonu
# -adres (geolokalizacjia)

# dla zamówień/rezerwacji:
# imię nazwisko klienta +
# nr telefonu (opcjonalnie) +
# adres e-mail +
# adres klienta (jeśli zamawia z dostawą)
# data/godzina złożenia zamówienia
# nazwa zamawianego leku 
# nazwa apteki w której zamówiono lek
# opłacono=tak/nie
# recepta=tak/nie
# refundacja
# cena zamówienia [zł]

# ilość leku dostępna w aptece