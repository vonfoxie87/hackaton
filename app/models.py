from enum import unique
from sqlalchemy import DateTime
from app import db
import datetime


class Zaak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100), unique=True, nullable=False)
    bvh = db.Column(db.Integer)
    zoekingen = db.relationship('Zoeking', backref='zoekingen')

    def __repr__(self):
        return f"Zaak: {self.naam}"


class Zoeking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100), unique=True, nullable=False)
    zoek_patroon = db.Column(db.String(100), unique=True, nullable=False)
    zoek_datum = db.Column(db.String(100))
    file_zoek = db.Column(db.String(100), unique=True, nullable=False)
    zaak_id = db.Column(db.Integer, db.ForeignKey('zaak.id'))

    def __repr__(self):
        return f"Zoeking: {self.naam}"


Zaak.zoekingen_query = db.relationship(Zoeking, lazy='dynamic')