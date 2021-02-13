# skrypt tworzący bazę danych
# to nie jest część projektu
from app import db

from models import *

# db.create_all()

# p = Pharmacy(name='Super Pharmacy', phone=777666555, adress="ul. Młynowa 60")

# d = Drug(name='Ketonal', size=50, power=100, state='tabs', prescription=True, refundation=0)

d1 = Drug(name='Allertec', size=100, power=1, state='syrop', prescription=False, refundation=30)
d2 = Drug(name='Zyrtec', size=20, power=10, state='tabs', prescription=True, refundation=0)
d3 = Drug(name='Groprinosin', size=20, power=500, state='tabs', prescription=False, refundation=0)
d4 = Drug(name='Apap', size=12, power=500, state='tabs', prescription=False, refundation=0)


db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.add(d4)
db.session.commit()

