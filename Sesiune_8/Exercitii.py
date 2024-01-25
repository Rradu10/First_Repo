'''
1. Scrieţi o funcţie care primeşte ca parametru
lungimea laturii unui pătrat şi returnează aria sa.
'''
# def aria_patrat(latura):
#     aria=latura**2
#     return aria
# aria=aria_patrat(12)
# print(aria)

'''
2. Scrieţi un subprogram care primeşte ca parametru lungimea laturii unui 
pătrat şi returnează atât lungimea diagonalei, cât şi perimetrul pătratului.
'''
# import math
# def diagonala_si_perimetrul(latura):
#     diagonala=latura*math.sqrt(2)
#     perimetrul=latura*4
#     return diagonala, perimetrul
#
# diagonala, perimetrul=diagonala_si_perimetrul(5)
# print(diagonala, perimetrul)



'''
3. Scrieţi o funcţie care primeşte ca parametri de intrare lungimile celor 
două catete ale unui triunghi dreptunghic şi returnează lungimea ipotenuzei.
'''
# import math
# def lungimea_ipotenuzei_dreptunghi(C1,C2):
#     ipotenuza=math.sqrt(C1**2+C2**2)
#     return ipotenuza
#
# ipotenuza=lungimea_ipotenuzei_dreptunghi(4,3)
# print(ipotenuza)

'''
4. Scrieţi o funcţie care primeşte 3 parametri de tip real, cu semnificaţia de 
lungimi pentru 3 segmente. Funcţia va returna 1 dacă cele trei segmente pot forma 
un triunghi şi 0, în caz contrar.
'''
# def triunghi_din_segmente(a,b,c):
#     if a + b > c and a + c > b and b + c > a:
#         return 1
#     return 0
#
# verificare=triunghi_din_segmente(3,6,4)
# print(verificare)


'''
 Sa se scrie o functie care primeste ca parametri 2
 numere si il returneaza pe cel mai mare
'''
# def cel_mai_mare(a,b):
#     return max(a,b)
# print(cel_mai_mare(10,123))


'''
6.Sa se scrie o functie care citeste de la tastatura un text si returneaza 
toate caracterele folosite in acel string ordonate alfabetic.
'''
def ordonarea_alfabetica(text):
    setul=set(text)
    lista_ordonata=sorted(setul)
    return lista_ordonata
text=input('Introduceti textul: ')
lista_caractere_ordonate=ordonarea_alfabetica(text)
print(lista_caractere_ordonate)

