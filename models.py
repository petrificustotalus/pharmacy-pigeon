from sqlalchemy import *

from app import db


class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    phone = db.Column(db.Integer)
    # that will be new separate table:
    adress = db.Column(db.String(140))
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 

    def __repr__(self):
        return f'<Pharmacy id: {self.id}, name: {self.name}>'

class Drug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))    
    size = db.Column(db.Integer)
    power = db.Column(db.Float)  
    state = db.Column(db.String(140))
    prescription = db.Column(db.Boolean)
    refundation = db.Column(db.Integer)

# dla 100 leków:
# -nazwa leku
# -wielkość opakowania  [oddzielna tabela]
# -cena dla każdej z aptek
# -ilość opakowań w każdej aptece
# -moc leku (mlg/ml)
# - postać leku
# -czy na recepte
# refundacja (-; 25%, 50%, 75%) [opisać logikę refundacji]

# dla 3 aptek:
# -nazwa apteki
# -nr telefonu
# -adres (geolokalizacjia)

# dla zamówień/rezerwacji:
# imię nazwisko klienta
# nr telefonu (opcjonalnie)
# adres e-mail
# data/godzina złożenia zamówienia
# nazwa zamawianego leku
# nazwa apteki w której zamówiono lek
# opłacono=tak/nie
# recepta=tak/nie
# refundacja
# cena zamówienia [zł]
