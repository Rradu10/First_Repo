import sqlite3

from Sesiune_19 import constants

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()
script = '''
CREATE TABLE IF NOT EXISTS Continents(
contient_id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT,
Code CHAR(2)); 
'''

cursor.execute(script)
conn.commit()
conn.close()
