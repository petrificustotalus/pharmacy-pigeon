import sqlite3

from .database_connection import DatabaseConnection


def create_meds_table() -> None:
    with DatabaseConnection('medsdata.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS meds(id integer primary key , nazwa text, postac text, dawka text,'
                       ' opakowanie text ,cena float )')


