# 1. if
a = 33
b = 200
if b > a:
    print('b este mai mare')

# 2. if ... else
if a > b:
    print('a este mai mare')
else:
    print('a este mai mic')

# 3. if...elif...else
if a > b:
    print('a este mai mare')
elif a < b:
    print('a este mai mic')
else:
    print('a este egal cu b')

# 4 if prescurtat
print('a') if a > b else print('b')
