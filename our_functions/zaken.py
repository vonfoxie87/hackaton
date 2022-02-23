import sqlite3


def create_zaak_table():
    db = sqlite3.connect("db.sqlite")
    db.execute('''CREATE TABLE IF NOT EXISTS zaken(id INTEGER PRIMARY KEY, naam TEXT)''')
    db.commit()


def create_zaak(naam):
    db = sqlite3.connect("../db.sqlite")
    cursor = db.cursor()
    cursor.execute('''INSERT INTO zaken(naam) VALUES(naam)''')
    db.commit()
    db.close()
    message = 'De nieuwe zaak is toegevoegd.'
    return message


def get_all_zaken():
    db = sqlite3.connect("../db.sqlite")
    cursor = db.cursor()
    cursor.execute('''SELECT naam FROM zaken''')
    all_rows = cursor.fetchall()
    db.close()
    return all_rows
    
