# skrypt tworzący bazę danych od 0
# to nie jest część projektu
from app import db

from models import *

# db.create_all()

# # Apteki
# p1 = Pharmacy(name='Super Pharmacy', phone=777666555, adress="ul. Młynowa 60")
# p2 = Pharmacy(name='New Pharmacy', phone=777666554, adress="ul. Młynowa 61")
# p3 = Pharmacy(name='Extra Pharmacy', phone=777666553, adress="ul. Młynowa 62")

# # Leki
# d = Druginfo(name='Ketonal', size=50, power=100, state='tabs', prescription=True, refundation=0)
# d1 = Druginfo(name='Allertec', size=100, power=1, state='syrop', prescription=False, refundation=30)
# d2 = Druginfo(name='Zyrtec', size=20, power=10, state='tabs', prescription=True, refundation=0)
# d3 = Druginfo(name='Groprinosin', size=20, power=500, state='tabs', prescription=False, refundation=0)
# d4 = Druginfo(name='Apap', size=12, power=500, state='tabs', prescription=False, refundation=0)

# # Ceny i dostępność
# price1 = DrugItem(druginfo_id=1, pharmacy_id=1, price=13, quantity=13)
# price2 = DrugItem(druginfo_id=1, pharmacy_id=2, price=13.90, quantity=12)
# price3 = DrugItem(druginfo_id=1, pharmacy_id=3, price=13.99, quantity=33)
# price4 = DrugItem(druginfo_id=2, pharmacy_id=1, price=3.46, quantity=10)
# price5 = DrugItem(druginfo_id=2, pharmacy_id=2, price=5.04, quantity=112)
# price6 = DrugItem(druginfo_id=2, pharmacy_id=3, price=4.99, quantity=3)

# db.session.add(p1, p2, p3)
# db.session.add(d, d1, d2, d3, d4)
# db.session.add(price1, price2, price3, price4, price5, price6)

# db.session.commit()


# W przyszłości należy zrobić 3 pliki csv - dla każdego z plików zrobić for loop, deklarujący zmienną, dodający i zapisujący w bazie danych

p4 = Pharmacy(name='Zaczptek', phone=777676666, adress="ul. Zamkowa 28")
db.session.add(p4)
db.session.commit()