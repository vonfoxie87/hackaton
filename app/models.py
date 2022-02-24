from sqlalchemy import PrimaryKeyConstraint
from app import db

class Zaak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100), unique=True, nullable=False)
    zoekingen = db.relationship('Zoeking', backref='zoekingen')

    def __repr__(self):
        return f"Zaak: {self.naam}"


class Zoeking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100), unique=True, nullable=False)
    zaak_id = db.Column(db.Integer, db.ForeignKey('zaak.id'))

    def __repr__(self):
        return f"Zoeking: {self.naam}"


Zaak.zoekingen_query = db.relationship(Zoeking, lazy='dynamic')