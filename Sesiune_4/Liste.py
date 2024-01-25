'''
Listele sunt folosite pentru a stoca mai multe valori intr-o singura variabila

Elemntele ditr-o lista sunt ordonabile, modificabile si permit valori duplicabile

Listele sunt indexate incepand de la 0

Cand spunem ca o lista este ordonata ne referim la faptul ca elementele au ordine predefinita si acea ordine nu se va schimba
'''

# creare
fructe = ['mere', 'pere', 'banane']
numere = [1, 2, 3, 4, 5]
masini = list(('audi', 'tesla', 'dacia'))

print(type(numere))
print(len(numere))

# indexare
print(20 * '-', 'indexare', 20 * '-')
print(numere[0])
print(numere[-1])
print(numere[:2])
print(numere[::2])

# adaugare element
print(20 * '-', 'adaugare element', 20 * '-')
numere.append(10)
print(numere)
numere.insert(2, 9)  # (index,element)
print(numere)

# stergere element
print(20 * '-', 'stergere element', 20 * '-')
elem = numere.pop()  # elimina de la final si il returneaza
print(elem)
print(numere)

numere.pop(0)  # elimina de la idexul specificat
print(numere)

numere.remove(3)  # elimina prima aparitie a valorii date
print(numere)

# stergere toate elementele
print(20 * '-', 'stergere toate elementele', 20 * '-')
numere.clear()
print(numere)

# inlocuire element
print(20 * '-', 'inlocuire element', 20 * '-')
print(fructe)
fructe[1] = 'struguri'
print(fructe)

# numararea aparitiei
print(20 * '-', 'numararea aparitiei', 20 * '-')
numere = [1, 2, 3, 4, 5]
print(numere.count(2))

# adunarea a 2 liste
print(20 * '-', 'adunarea a 2 liste', 20 * '-')
numere2 = [20, 21, 22]
numere.extend(numere2)
print(numere)
numere3 = [1, 2, 3]
print(numere2 + numere3)  # Nu se modifica niciuna din cele 2 liste

# inversare
print(20 * '-', 'inversare', 20 * '-')
# 1
print(fructe[::-1])  # Nu modifica lista initiala
# 2
fructe.reverse()
print(fructe)  # Modifica lista initiala  (operatiune de in place)

# sortare
print(20 * '-', 'sortare', 20 * '-')
numere.sort()
print(numere)
numere.sort(reverse=True)
print(numere)
