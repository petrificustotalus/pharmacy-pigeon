# skrypt tworzący bazę danych od 0
# to nie jest część projektu
from medivisor import db

from medivisor.models import *

db.create_all()

# # Apteki
p1 = Pharmacy(name='Super Pharmacy', phone=777666555, adress="ul. Młynowa 60")
p2 = Pharmacy(name='New Pharmacy', phone=777666554, adress="ul. Młynowa 61")
p3 = Pharmacy(name='Extra Pharmacy', phone=777666553, adress="ul. Młynowa 62")

# Usuwanie item:
# drug1 = DrugItem.query.filter(DrugItem.id == 1).first()
# db.session.delete(drug1)


# # Leki
d = Druginfo(name='ketonal', size=50, power=100, state='tabs', prescription=True, refundation=0)
d1 = Druginfo(name='allertec', size=100, power=1, state='syrop', prescription=False, refundation=30)
d2 = Druginfo(name='zyrtec', size=20, power=10, state='tabs', prescription=True, refundation=0)
d3 = Druginfo(name='groprinosin', size=20, power=500, state='tabs', prescription=False, refundation=0)
d4 = Druginfo(name='apap', size=12, power=500, state='tabs', prescription=False, refundation=0)

# # Ceny i dostępność
price1 = DrugItem(druginfo_id=1, pharmacy_id=1, price=13, quantity=13)
price2 = DrugItem(druginfo_id=1, pharmacy_id=2, price=13.90, quantity=12)
price3 = DrugItem(druginfo_id=1, pharmacy_id=3, price=13.99, quantity=33)
price4 = DrugItem(druginfo_id=2, pharmacy_id=1, price=3.46, quantity=10)
price5 = DrugItem(druginfo_id=2, pharmacy_id=2, price=5.04, quantity=112)
price6 = DrugItem(druginfo_id=2, pharmacy_id=3, price=4.99, quantity=3)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

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


# db.session.commit()


# # W przyszłości należy zrobić 3 pliki csv - dla każdego z plików zrobić for loop, deklarujący zmienną, dodający i zapisujący w bazie danych

# p4 = Pharmacy(name='Zaczptek', phone=777676666, adress="ul. Zamkowa 28")
# db.session.add(p4)
db.session.commit()
