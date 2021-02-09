# skrypt tworzący bazę danych
# to nie jest część projektu
from app import db

from models import *

db.create_all()

# p = Pharmacy(name='Super Pharmacy', phone=777666555, adress="ul. Młynowa 60")

# d = Drug(name='Ketonal', size=50, power=100, state='tabs', prescription=True, refundation=0)

c = Client(name='John', surname='Doe', phone =717171717)

db.session.add(c)
db.session.commit()

