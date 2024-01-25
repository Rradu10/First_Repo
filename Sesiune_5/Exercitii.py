'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă.
'''
l1=[3, 1, 0, 2]
l2=[6, 5, 4]
lista=l1+l2
# l1.extend(l2)
# print (l1)



'''
4.
Sortează și afișează lista generată la exercițiul anterior.
Elimina numărul 0 folosind o funcție.
Afișaza iar lista.
'''
lista.sort()
print(lista)
lista.remove(0)
print(lista)



'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.
'''

lista=l1+l2
if(len(lista)==0):
    print("Lista este goala")
if(lista==[]):
    print("Lista este goala")
if not lista:
    print("Lista este goala")


if(len(lista)!=0):
    print("Lista nu este goala")
if(lista!=[]):
    print("Lista nu este goala")
if lista:
    print("Lista nu este goala")

'''
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
'''
lista.clear()
'''
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
'''
if(len(lista)==0):
    print("Lista este goala")
else:
    print("Lista nu este goala")


'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
print(dict1.keys())


'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
nume=input('Introdu un nume: ')
nota=dict1.get(nume)
if nota is None:
    print('Ai introdus o valoare incorecta')
else:
    print(f'{nume} a luat nota {nota}')




'''
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare
'''
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}

dict1['Dorel'] = 6
print(dict1['Dorel'])




'''
11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
'''
dict1.pop('Gigel')
print(dict1)
dict1['Ionica']=9
print(dict1)




'''
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add('luni')  # nu se adauga pt ca deja exista in set
print(zile_sapt)



'''
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}


if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')




'''
15. Afișează diferențele dintre aceste 2 seturi.
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}


print(zile_sapt.difference(weekend))
print(zile_sapt - weekend)





'''
16. Afișează intersecția elementelor din aceste 2 seturi.
'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt.intersection(weekend))
print(zile_sapt & weekend)
