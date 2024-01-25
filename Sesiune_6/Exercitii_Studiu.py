'''

1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.

'''
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(mașini)):
#     print(mașini[i])
#     if mașini[i]=='Mercedes':
#         masina_pref=mașini[i]
# print(f'Masina mea preferata este {masina_pref}')

# for i in mașini:
#     if i == 'Mercedes':
#         masina_pref=i
#     print(i)
# print(f'Masina mea preferata este {masina_pref}')

# index=0
# while index<len(mașini):
#     print(mașini[index])
#     if mașini[index]=='Aston Martin':
#         masina_pref=mașini[index]
#     index+=1
# print(f'Masina mea preferata este {masina_pref}')

'''
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
'''
for i in range(1,len(mașini)-1):
    mașini[i]=mașini[i].upper()
else:
    print(mașini)
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']




'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
'''
# for masina_dorita in mașini:
#     if masina_dorita == 'Mercedes':
#         print('Am gasit masina dorită de dvs')
#         break
#     else:
#         print(f'Am gasit masina {masina_dorita}. Mai cautam.')




'''
4. Aceeasi lista
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
'''
for masina in mașini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina {masina}')
