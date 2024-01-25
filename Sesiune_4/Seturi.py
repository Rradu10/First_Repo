# Seturile sunt colectii de elemente unice si neordonabile

# creare
fructe = {'mar', 'para', 'banana'}
masini = set()  # Asa se creaza un set fara niciun element

# adaugare elemente
print(20 * '-', 'adaugare elemente', 20 * '-')
fructe.add('struguri')
print(fructe)

# stergere elemente
print(20 * '-', 'stergere elemente', 20 * '-')
fructe.remove('banana')
print(fructe)

# fructe.remove('cirese') - Arunca eroare pt ca nu exista 'cirese' in set
fructe.discard('cirese')  # Nu arunca eroare

fructe.pop()
print(fructe)

fructe.clear()
print(fructe)

# Operatii speciale
print(20 * '-', 'Operatii speciale', 20 * '-')

# 1. Join
print(20 * '-', 'Join', 20 * '-')

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print(set1 | set2)

# 2. Intersectia
print(20 * '-', 'Intersectia', 20 * '-')

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y)
print(z)
print(x & y)

# 3.Diferenta
print(20 * '-', 'Diferenta', 20 * '-')
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.difference(y)
print(z)
print(x - y)
print(y - x)

# 4.Diferenta simetrica
print(20 * '-', 'Diferenta simetrica', 20 * '-')
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.symmetric_difference(y)  # Toate elementele care nu sunt comune
print(z)
print(x ^ y)

# 5.Subset si Superset
print(20 * '-', 'Subset si Superset', 20 * '-')
a = {1, 2, 3}
b = {5, 4, 3, 2, 1}
print(a.issubset(b))  # Toate elementele lui a sunt in b
print(b.issuperset(a))  # b contine toate elementele lui a
