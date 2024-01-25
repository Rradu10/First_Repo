'''
21. Având stringul '0123456789'
Afișează doar numerele pare
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
'''
# string='0123456789'
# print(string[::2])
# print(string[1::2])


'''
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''
# string = input('Introdu stringul: ')
# assert string[0].lower()==string[-1].lower()


'''
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''
# import random
# dice_roll=random.randint(1,6)
# ghici=int(input('Alege un numar intr 1 si 6: '))
# if ghici<dice_roll:
#     print(f'Ai pierdut. Ai aes un numar mai mic. Ai ales {ghici} dar a fost {dice_roll}.')
# elif ghici>dice_roll:
#     print(f'Ai pierdut. Ai aes un numar mai mare. Ai ales {ghici} dar a fost {dice_roll}.')
# else:
#     print(f'Ai ghicit. Felicitari! Ai ales {ghici} si zarul a fost {dice_roll}.')


'''
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
-Citește de la tastatură un int x
-Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
# string = 'Coral is either the stupidest animal or the smartest rock'
# x=int(input(f'Alege un numar intre 1 si {len(string)} : '))
# # y=len(string)-x
# # print(string[:y])
# print(string[:-x])


'''
8. 
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
# x=int(input('x = '))
# y=int(input('y = '))
# z=int(input('z = '))
# if x==y==z:
#     print('Triunghiul este echilateral')
# elif x!=y!=z:
#     print('Triunghiul este oarecare')
# else:
#     print('Triunghiul este isoscel')


'''
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.
'''
# litera = input('Scrie o litera -> ')
# if litera.lower() in 'aeiou':
#     print('Litera este vocala')
# else:
#     print('Litera este consoana')


'''
10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
# nota=float(input('Nota in sistem romanesc = '))
# if nota>9:
#     print('Nota se transforma in A')
# elif nota>8:
#     print('Nota se transforma in B')
# elif nota>7:
#     print('Nota se transforma in C')
# elif nota>6:
#     print('Nota se transforma in D')
# elif nota>4:
#     print('Nota se transforma in E')
# else:
#     print('Nota se transforma in F')


'''
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

# x = int(input("x= "))
# if x>999:
#     print(f"{x} are cel putin 4 cifre.")
# else:
#     print(f"{x} nu are cel putin 4 cifre.")


'''
12.Verifică dacă x are exact 6 cifre.
'''
# x = int(input("x= "))
# if 99999<x<1000000:
#     print(f"{x} are exact 6 cifre.")
# else:
#     print(f"{x} nu are exact 6 cifre.")


'''
13.Verifică dacă x este număr par sau impar (x e int).
'''
# x = int(input("x= "))
# if x%2==0:
#     print(f'{x} este par')
# else:
#     print(f'{x} este impar')


'''
14.      x, y, z (int)
Afișează care este cel mai mare dintre ele?
'''
# x=int(input('x = '))
# y=int(input('y = '))
# z=int(input('z = '))
# aux=max(x,y,z)
# print(f"Cel mai mare numar dintre {x}, {y} si {z} este {aux}.")


'''
15. 
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu
'''
# x = float(input("Unghiul x= "))
# y = float(input("Unghiul y= "))
# z = float(input("Unghiul z= "))
# if x+y+z==180:
#     print('Unghiurile formeaza un triunghi valid')
# else:
#     print('Unghiurile nu formeaza un triunghi valid')






'''
17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
'''
# string = 'Coral is either the stupidest animal or the smartest rock'
# string1 = string[:5]+string[-5:]
# print(string1)





'''
18. Același string. 
-Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
-Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
-output: 'Coral is either the stupidest animal or the smartest' 
'''
# string= 'Coral is either the stupidest animal or the smartest rock'
# rock=string.find('rock')
# print(string[:rock])
