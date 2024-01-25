# Structura if else este o conditie care daca nu indeplineste prima dorinta o va lua pe urmatoarea care este scrisa dupa "else"

#2
x=3
if type(x)==int and x>=0:
    print('x este un numar natural')

#3
y=-12
if y>0:
    print('y este un numar pozitiv')
elif y<0:
    print('y este un numar negativ')
else:
    print('y este un numar neutru)')

#4
print('x este intre -2 si 13') if -2<=x<=13 else print('x nu este intre -2 si 13')

#5
print('x-y<5') if x-y<5 else print('x-y>5')

#6
if x not in 5<=x<=27:
    print('x nu este între 5 și 27')

#7
a=int(13.99)
b=int(13.00)
if a==b:
    print('a este egal cu b')
elif a<b:
    print('b este mai mare decat a')
else:
    print('a este mai mare decat b')
