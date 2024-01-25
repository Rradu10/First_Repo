import sqlite3
from pprint import pprint

conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

cursor.execute('''
insert into Users (username, email, password, first_name, last_name, address, city, postal_code, country)
Values ("AndreiAdi", "andrei@gmail.com", "parolaAndrei", "Andrei", "Lapusanu", "Str. Observatorului", "Cluj-Napoca", 400281, "RO");
''')


cursor.execute('''
insert into Users (username, email, password, first_name, last_name, address, city, postal_code, country)
Values ("ValentinaV", "vale@gmail.com", "parolaVale", "Valentina", "Lapusanu", "Str. Observatorului", "Cluj-Napoca", 400281, "RO");
''')
conn.commit()
cursor.execute('select * from Users;')
pprint(cursor.fetchall())
