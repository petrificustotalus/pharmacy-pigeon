import sqlite3
from typing import List, Dict, Union
from .database_connection import DatabaseConnection

Med = Dict[int, str, str, str, str, float]  # new typing type


def create_meds_table() -> None:
    with DatabaseConnection('medsdata.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS meds(id integer primary key , nazwa text, postac text, dawka text,'
                       ' opakowanie text ,cena float )')


def add_med_to_the_table(id: int, nazwa: str, postac: str, dawka: str, opakowanie: str, cena: float) -> None:
    try:
        with DatabaseConnection('medsdata.db') as connection:
            cursor = connection.cursor()

            cursor.execute(f'INSERT INTO meds VALUES(?, ?, ?, ?, ?, ?) ', (id, nazwa, postac, dawka, opakowanie, cena))
            """
             Can I use generator here to generates id, except add it to the function 
             that will collect all the properties from scrapper?? I don't know what to do with id yet :(
            """

    except sqlite3.IntegrityError:
        print('\nthis is information from me to me that the id crashed, witch probably will happen')


def get_all_meds() -> List[Med]:
    with DatabaseConnection('medsdata.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM meds')
        meds = [{'id': row[0], 'nazwa': row[1], 'postac': row[2], 'dawka': row[3], 'opakowanie': row[4], 'cena': row[5]} for row in cursor.fetchall()]
        # cursor.fetchall() --> [(id, nazwa, postac, dawka, opakowanie, cena), (id, nazwa, postac, ...), ...]

    return meds