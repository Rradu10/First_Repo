'''
Sa se scrie un program care citeste numere de la tastatura pana cand se introduce numarul 0.
Pentru fiecare numar introdus se verifica daca este par,
iar la final se vor afisa intr-o lista toate numerele pare.
'''
# x=-1
# # rezultat=[]
# # while x:
# #     x=int(input('Introdu un numar'))
# #     if x%2==0:
# #         rezultat.append(x)
# # print(rezultat)




'''
Sa se scrie un program care citeste un text de la tastatura si 
va afisa un dictionar cu toate caracterele din text in care cheile vor fi 
caracterele, si valorile daca caracterul cheie este vocala sau consoana.
'''
text=input('Introdu un text: ')
dct={}
for char in text:
    if not char.is():
        continue
    char_type = 'vocala' if char.lower() in 'aeiou' else 'consoana'
    dct[char]=char_type
print(dct)

