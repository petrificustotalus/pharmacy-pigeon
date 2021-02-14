# skrypt tworzący bazę danych
# to nie jest część projektu
from app import db

from models import *

db.create_all()

# prices.__table__.create(db.session.blind)

# p = Pharmacy(name='Super Pharmacy', phone=777666555, adress="ul. Młynowa 60")

d = Druginfo(name='Ketonal', size=50, power=100, state='tabs', prescription=True, refundation=0)
d1 = Druginfo(name='Allertec', size=100, power=1, state='syrop', prescription=False, refundation=30)
d2 = Druginfo(name='Zyrtec', size=20, power=10, state='tabs', prescription=True, refundation=0)
d3 = Druginfo(name='Groprinosin', size=20, power=500, state='tabs', prescription=False, refundation=0)
d4 = Druginfo(name='Apap', size=12, power=500, state='tabs', prescription=False, refundation=0)

# p1 = Pharmacy(name='New Pharmacy', phone=777666543, adress="ul. Młynowa 61")
# p2 = Pharmacy(name='Extra Cool Pharmacy', phone=777666531, adress="ul. Młynowa 62")
price1 = DrugItem(druginfo_id=1, pharmacy_id=1, price=13, quantity=13)
price2 = DrugItem(druginfo_id=1, pharmacy_id=2, price=13.90, quantity=12)
price3 = DrugItem(druginfo_id=1, pharmacy_id=3, price=13.99, quantity=33)
price4 = DrugItem(druginfo_id=2, pharmacy_id=1, price=3.46, quantity=10)
price5 = DrugItem(druginfo_id=2, pharmacy_id=2, price=5.04, quantity=112)
price6 = DrugItem(druginfo_id=2, pharmacy_id=3, price=4.99, quantity=3)

db.session.add(d)
db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.add(d4)
db.session.add(price1)
db.session.add(price2)
db.session.add(price3)
db.session.add(price4)
db.session.add(price5)
db.session.add(price6)
db.session.commit()

