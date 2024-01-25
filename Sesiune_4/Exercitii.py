'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
-Afișeaz-o.
-Inversează ordinea folosind slicing și suprascrie această listă.
-Printează varianta actuală (inversată).
-Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
-Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
'''
note_muzicale=['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
inv=note_muzicale[::-1]
print(inv)
inv.reverse()
print(inv)


#2.
print(inv.count('do'))

#3 Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.
note=('do','re','mi','fa','sol','la','si','do')
note+=('do',)
print(note)

'''
4. Declara un dictionar cu notele muzicale de mai sus. 
Cheia va fi nota, iar valoarea un numar care arata de cate ori apare nota in gama. 
Afiseaza-l.
'''

note= {
    'do':2,
    're':1,
    'mi':1,
    'fa':1,
    'sol':1,
    'la':1,
    'si':1
      }
print(note)
