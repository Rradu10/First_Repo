# Lungimea unui string

name = 'Dragos '
print(len(name))

# Convertire la uppercase

print(name.upper())

name = 'dRaGoS'
# Convertire la lowercase
print(name.lower())

# Numar de aparitii

nume = 'Ana Maria'
print(nume.count('a'))

# inlocuire de text
prop = ' - oare vreau sa merg acolo! \n - unde sa mergi!'
# \n- caracter pt linie noua
print(prop)

print(prop.replace('!','?'))
print(prop)

# index

name = 'john'
print(name.index('o'))  # gaseste indexul primei potriviri cu caracterul din paranteza
print(name[0])

print(name[-1])

# slicing

b = 'hello, world!'
print(b[2:5])  # de la 2 la 5 (fara 5)
print(b[:5])  # de la inceput pana la 5
print(b[5:])  # de la 5 pana la sfarsit
print(b[-5:-2])
