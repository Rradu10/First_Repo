# creare
car = {
    'brand': 'ford',
    'model': 'mustang',
    'an': '1962'
}

# accesare elemente
print(20 * '-', 'accesare elemente', 20 * '-')
print(car['brand'])
print(car.get('model'))
print(car.get('is_new'))
print(car.get('is_new', True))

# adaugare elemente
print(20 * '-', 'adaugare elemente', 20 * '-')
car['is_new'] = True
print(car)

car.setdefault('is_new',True)  # Returneaza valoarea de la cheia data, iar daca aceasta nu exista o adauga cu valoarea True (valoarea din paranteze)
car.setdefault('price', 7910)
print(car)

# stergere element
print(20 * '-', 'stergere elemente', 20 * '-')
car.pop('is_new')
print(car)

car.popitem()  # Elimina ultima cheie inserata
print(car)

del car['an']
print(car)

# stergerea tuturor elementelor
print(20 * '-', 'stergerea tuturor elementelor', 20 * '-')
car.clear()
print(car)

# afisare toate chei
print(20 * '-', 'afisare toate chei', 20 * '-')
car = {
    'brand': 'ford',
    'model': 'mustang',
    'an': 1962
}
print(list(car.keys()))
# afisare toate valori
print(list(car.values()))

# afisare toate elemente
print(20 * '-', 'afisare toate elemente', 20 * '-')
print(list(car.items()))
