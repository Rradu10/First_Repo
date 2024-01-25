#Sa se scrie un program care citeste un text de la tastatura si afiseaza o lista cu
#fiecare caracter in ordinea inversa a aparitiei in text.
# cuvant = input('Introdu un cuvant: ')
#
# l = list(cuvant)
#
# print(l[::-1])


'''
2. Sa se scrie un program care citeste numele, emailul si varsta unei persoane de la tastatura si adauga toate datele intr-un dictionar pe care il afiseaza.
    Daca persoana nu este multumita cu datele introduse va putea specifica daca vrea sa modifice maxim o valoare din dictionar.
'''
# nume=input('introdu numele: ')
# email=input('introdu email: ')
# varsta=input('introdu varsta: ')
# data= {
#     'nume':nume,
#     'email':email,
#     'varsta':varsta
# }
# print(data)
#
# modifica= input('Vrei sa modifici datele? (y/n)')
# if modifica=='y':
#     cheie_de_modificat=input('Introdu cheia pe care vrei sa o modifici: ')
#     if cheie_de_modificat not in data:
#         print('Nu exsita aceasta valoare!')
#     else:
#         valoare_de_modificat=input('Introdu noua valoare:')
#         valoare_de_modificat=int(valoare_de_modificat) if cheie_de_modificat=='varsta' else valoare_de_modificat
#         data[cheie_de_modificat]=valoare_de_modificat
# print(data)




'''
3. Fie seturile:
    
    set1 = {"Yellow", "Orange", "Black"}
    set2 = {"Orange", "Blue", "Pink"}
    
    
    1. Sa se afiseze toatele elementele care apar in `set1` si nu apar in `set2`
    2. Sa se afiseze toatele elementele care apar in ambele seturi
    3. Sa se afiseze toatele elementele care nu sunt comune
'''
# set1 = {"Yellow", "Orange", "Black"}
# set2 = {"Orange", "Blue", "Pink"}
# print(set1 - set2)#1
# print(set1 & set2)#2
# print(set1 ^ set2)#3






'''
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișează ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișează ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”
'''


teren = ['Messi', 'Ronaldo', 'Mbape', 'Haaland', 'Muller']
schimbari_efectuate = 3
schimbari_max = 3
jucator=input('Alegeti u jucator pe care vreti sa-l schimbati: ')
if jucator in teren:
    if schimbari_efectuate<schimbari_max:
        teren.remove(jucator)
        jucator_intrat=input('Alegeti un jucator care vreti sa intre in teren: ')
        teren.append(jucator_intrat)
        schimbari_efectuate+=1
        print(f'A intrat {jucator_intrat}, a iesit {jucator}, mai ai {schimbari_max-schimbari_efectuate} schimbari disponibile')
    else:
        print('Ai folosit toate schimbarile disponibile.')
else:
    print(f'Nu se poate efectua schimbarea deoarece {jucator} nu e in teren. Mai ai {schimbari_max - schimbari_efectuate} schimbari disponibile.')
