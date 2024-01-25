import sqlite3

conn = sqlite3.connect('clasaelevi.db')
cursor = conn.cursor()
script = '''
CREATE TABLE IF NOT EXISTS Elevi(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
grade REAL DEFAULT 0,
absences INTEGER DEFAULT 0);
'''
cursor.executescript(script)

# cursor.execute('''
# insert into Elevi (name, grade, absences)
# Values ("Abarzaei Rares", "10", "19");
# ''')
# cursor.execute('''
# insert into Elevi (name, grade, absences)
# Values ("Abarzaei Rares", "10", "19");
# ''')
#
# conn.commit()
# cursor.execute('select * from Elevi;')
# pprint(cursor.fetchall())


