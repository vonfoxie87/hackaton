import sqlite3
from flask import request


def create_zaak_table():
    db = sqlite3.connect("../db.sqlite")
    cursor = db.cursor()
    # create table zaken if not exsist
    cursor.execute('''CREATE TABLE IF NOT EXISTS zaken(id INTEGER PRIMARY KEY, naam TEXT)''')
    db.commit()


def create_zaak():
    # db connectie
    db = sqlite3.connect("../db.sqlite")
    cursor = db.cursor()
    # create table zaken if not exsist
    cursor.execute('''CREATE TABLE IF NOT EXISTS zaken(id INTEGER PRIMARY KEY, naam TEXT)''')
    db.commit()
    # insert new zaak
    naam = request.POST.get('naam')
    cursor.execute('''INSERT INTO zaken(naam) VALUES(?)''', (naam))
    db.commit()
    db.close()
    message = 'De nieuwe zaak is toegevoegd.'
    return message


def get_all_zaken():
    create_zaak_table()
    db = sqlite3.connect("../db.sqlite")
    cursor = db.cursor()
    cursor.execute('''SELECT naam FROM zaken''')
    all_rows = cursor.fetchall()
    db.close()
    return all_rows

