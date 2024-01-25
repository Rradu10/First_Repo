# csv = comma separated values
import csv
from pprint import pprint

from tabulate import tabulate

def read(filename):
    with open(filename,'r') as f:
        reader = csv.reader(f) # este iterator peste toate liniile din fisierul f si returneaza fiecare linie ca lista de valori
        return list(reader)

print(read('angajati.csv'))
reader = read('angajati.csv')
print(reader)
tabel = tabulate(reader[1:],headers=reader[0])
print(tabel)

def write(filename,data):
    with open(filename,'w') as f:
        writer=csv.writer(f)
        writer.writerows(data)

data = [
    ["Nume", "Varsta"],
    ["Sergiu", "25"],
    ["Andrei", "30"],
    ["Cristi", "34"]
]
write('persoane.csv',data)
print(read('persoane.csv'))

def read_dict(filename):
    with open(filename,'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
pprint(read_dict('angajati.csv'))


def write_dict(filename,data):
    with open(filename,'w') as f:
        writer=csv.DictWriter(f,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

data2=[
    {"Nume": "Sergiu", "Varsta": "25"},
    {"Nume": "Andrei", "Varsta": "31"},
    {"Nume": "Dan", "Varsta": "45"}

]
pprint(write_dict('persoane.csv',data2))
