'''
O clasa este o schita sau un prototip definit de programator din care sunt create obiecte.
Clasele ofera un mijloc de a grupa datele si functionalitatile.
Clasele noi creaza un nou tip de de obiect, permitand instantierea unor obiecte din acest tip
Fiecare instanta de clasa poate avea atribute atasate pt mentiearea starii sale
Instantele de clasa pot avea si metode pentru modificarea starii lor.
Un obiect este instanta unei clase. Diferenta dintre obiect si clasa: - o clasa este ca o schita
                                                                      - un obiect este o copie a clasei cu valori reale
'''

class Dog:
    species='mamifer'
    age='8'
    name='Bruno'
d=Dog()#instantierea unui obiect(d=>obiect)
print(type(d))
print(d.species)
print(d.age)
print(d.name)

d2=Dog()
d2.name='Puffy' # name devine atribut de instanta pt obiectul d2 (nu se mai modifica decat prin d2)
print(d.name,d2.name)
Dog.name='Rexy'
print(d.name,d2.name)

#atributele de clasa sunt in general folosite pt a defini constante intr-o clasa

class Cat:
    species='mamifer'
    def __init__(self,age,name): # functie constructor
        #self este o referinta catre obiectul curent
        self.age=age
        self.name=name

c=Cat(1,'Leo')
c2=Cat(4,'Nita')
print(c.age,c2.age)

# Cat.name # --> incorect deoarece atributul name este un atribut de instanta
# si poate fi accesat doar printr-un obiect din aceasta clasa
