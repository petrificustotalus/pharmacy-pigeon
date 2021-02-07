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