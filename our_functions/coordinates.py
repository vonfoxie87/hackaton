import pandas as pd
import sqlite3


def get_coordinates():
    df = pd.read_csv('data/coordinaten.csv')
    print(df)
