# skrypt tworzący bazę danych
# to nie jest część projektu
from app import db

from models import *

db.create_all()

# p = Pharmacy(name='Super Pharmacy', phone=777666555, adress="ul. Młynowa 60")

# db.session.add(p)
# db.session.commit()

d = Drug(name='Ketonal', size=50, power=100, state='tabs', prescription=True, refundation=0)
db.session.add(d)
db.session.commit()