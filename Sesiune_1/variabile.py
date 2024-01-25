# variabila - container de memorie pt a stoca valori

# 1 - crearea unei variabile

x = 5  # se ia o zona din memorie in care se pune valoarea 5
y = 'john'  # ------//--------

print(x)
print(y)

# 2. denumirea variabilelor
'''
reguli:
-numele variabilei trebuie sa inceapa cu o litera sau "_"
-numele variabilei nu poate incepe cu un nr.
-numele variabilei poate contine doar caractere alfa numerice si _
-numele variabilei sunt case sensitive (age, AGE, Age sunt 3 variabile diferite)
'''
# asa DA
myvar = 'Dina'
my_var = 'Dina'
_my_var = 'Dina'
myVar = 'Dina'
myvar2 = 'Dina'

# asa NU
'''
2myvar='Dina'
my-var='Dina'
my var='Dina'
'''

# 3. Multiple valori la multiple variabile
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

# 4. O valoare multiple variabile
x = y = z = 'portocala'
print(x)
print(y)
print(z)

#   CTRL + ALT + L  -- Beautify
