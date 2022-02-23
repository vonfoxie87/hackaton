import sqlite3


def create_zaak_table():
    db = sqlite3.connect("db.sqlite")
    db.execute('''CREATE TABLE IF NOT EXISTS zaken(naam text)''')
    db.commit()
    db.close()


def create_zaak(naam):
    db = sqlite3.connect("db.sqlite")
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO zaken VALUES('{naam}')")
    db.commit()
    db.close()
    message = 'De nieuwe zaak is toegevoegd.'
    return message


def get_all_zaken():
    db = sqlite3.connect("db.sqlite")
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM zaken''')
    all_rows = cursor.fetchall()
    db.close()
    return all_rows
