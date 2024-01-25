'''
Cu o bucla while putem executa un set de instructiuni pana ce o conditie este adevarata
'''
count = 0
while count < 3:
    count += 1
    print(f'Count: {count}')

l = [1, 2, 3, 4, 5]
index = 0
while index < len(l):
    print(l[index])
    index += 1
print(20 * '-')
# break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # opreste iteratia
    i += 1

print(20 * '-')
# Continue

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # sare peste codul de sub el si merge la urmatoarea verificare a conditiei din while
    print(i)

print(20 * '-')
# Else
count = 0
while count < 3:
    count += 1
    print(f'Count: {count}')
else:  # ruleaza cand bucla se termina
    print('Sunt in else')

print(20 * '-')
# Else + break

count = 0
while count < 3:
    count += 1
    print(f'Count: {count}')
    if count == 1:
        break
else:  # ruleaza cand apare break in while
    print('Sunt in else')

print(20 * '-')
