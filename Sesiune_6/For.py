'''
O bucla for este folosita pentru a itera peste o secventa (lista, tuplu, dictionar, set, string)
'''
for i in range(10):
    print(i)
print(20 * '-')
for i in range(4, 10):
    print(i)
print(20 * '-')
for i in range(4, 10, 2):
    print(i)

print(20 * '-')
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(l[i])

print(20 * '-')
# for each
fructe = ['mere', 'pere', 'banane']
for x in fructe:
    print(x)

print(20 * '-')
for x in 'Ana are mere':
    print(x)

print(20 * '-')
d = {
    'a': 1,
    'b': 2
}
for x in d:  # iterarea in dictionar se face implicit prin chei
    print(x)
for x, value in d.items():
    print(x, value)

print(20 * '-')
# continue
for x in fructe:
    if x == 'mere' or x == 'pere':
        continue
    print(x)

print(20 * '-')
# else
for x in fructe:
    print(x)
else:
    print('Sunt in else')

# else + break
for x in fructe:
    if x == 'pere':
        break
else:
    print('Sunt in else')

print(20 * '-')
# nested for

adj = ['rosii', 'mari', 'delicioase']
for x in fructe:
    for y in adj:
        print(x, y)

print(20 * '-')
# pas
for x in range(100_000_000):
    pass
print('gata')
