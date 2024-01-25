'''
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''
import math
class Circle:
    def __init__(self,radius,color):
        self.radius=radius
        self.color=color

    def descriere_cerc(self):
        print(f'Raza : {self.radius}, Culoare: {self.color}')

    def aria(self):
        return math.pi * self.radius**2

    def diametru(self):
        return 2 * self.radius

    def circumferinta(self):
        return 2 * math.pi * self.radius

c=Circle(5,'albastru')
print(c.descriere_cerc())
print(c.aria())
print(c.diametru())
print(c.circumferinta())












'''
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
'''
class Dreptunghi:
    def __init__(self,L,l,culoare):
        self.L=L
        self.l=l
        self.culoare=culoare
    def descriere(self):
        return f'Lungimea: {self.L}, Latimea: {self.l}, Culoare: {self.culoare}'
    def aria(self):
        return self.L*self.l
    def perimetrul(self):
        return 2*(self.L+self.l)
    def schimba_culoarea(self,noua_culoare):
        self.culoare=noua_culoare

d=Dreptunghi(6,8,'albastru')
print(d.descriere())
d.schimba_culoarea('verde')
print(d.aria())
print(d.perimetrul())
print(d.descriere())
