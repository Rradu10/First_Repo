import sqlite3
from pprint import pprint

conn = sqlite3.connect('clasaelevi.db')
cursor = conn.cursor()

def adauga_elev(name, grade, absences):
    cursor.execute('Insert into Elevi(name, grade, absences) Values (?,?,?)', [name, grade, absences])
    conn.commit()


another = 'y'
while another == 'y':
    nume_elev = input('Introduceti numele elevului: ')
    nota_elev = input('Introduceti nota elevului: ')
    absente_elev = input('Introduceti numarul de absente ale elevului: ')
    adauga_elev(nume_elev, nota_elev, absente_elev)
    another = input('Doriti sa mai adaugati un elev? (y/n) : ')

cursor.execute('select * from Elevi;')
pprint(cursor.fetchall())
