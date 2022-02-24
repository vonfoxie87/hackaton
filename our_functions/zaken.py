import sqlite3
from flask import request, render_template


def create_zaak_table():
    db = sqlite3.connect("db.sqlite")
    db.execute('''CREATE TABLE IF NOT EXISTS zaken(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                   naam TEXT,
                                                   bvh TEXT,
                                                   naam_zoekpatroon TEXT,
                                                   datum DATE,
                                                   zaak_id INTEGER,
                                                   file_zoekpatroon TEXT
                                                   )''')
    db.commit()
    db.close()


def create_zaak(naam):
    db = sqlite3.connect("db.sqlite")
    cursor = db.cursor()
    cursor.execute('INSERT INTO zaken(naam) VALUES(?)', (naam,))
    db.commit()
    db.close()
    message = 'De nieuwe zaak is toegevoegd.'
    return message


def create_zoekpatroon(id_zoek, naam, naam_zoek, datum_zoek, file_zoek):
    db = sqlite3.connect("db.sqlite")
    cursor = db.cursor()
    cursor.execute('INSERT INTO zaken(naam, naam_zoekpatroon, datum, zaak_id, file_zoekpatroon) VALUES(?, ?, ?, ?, ?)', (naam, naam_zoek, datum_zoek, id_zoek, file_zoek))
    db.commit()
    db.close()
    message = 'De nieuwe zoekpatroon is toegevoegd.'
    return message


def get_all_zaken():
    db = sqlite3.connect("db.sqlite")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM zaken WHERE zaak_id IS NULL or zaak_id = id")
    all_rows = cursor.fetchall()
    db.close()
    return all_rows


def get_zoekpatronen(id_zoek):
    id_zoek = int(id_zoek)
    print(id_zoek)
    db = sqlite3.connect("db.sqlite")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM zaken WHERE zaak_id=? OR id=?", (id_zoek,id_zoek))
    zaak_rows = cursor.fetchall()
    db.close()
    return zaak_rows


def get_zoekpatronen_empty(id):
    id = int(id)
    print(id)
    db = sqlite3.connect("db.sqlite")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM zaken WHERE id=?", (id,))
    zaak_rows = cursor.fetchall()
    db.close()
    return zaak_rows