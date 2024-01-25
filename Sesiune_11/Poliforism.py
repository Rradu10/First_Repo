class Animal:
    def __init__(self, age, specie):
        self.age = age
        self.specie = specie

    def eat(self):
        return f'Eu sunt un {self.__class__.__name__}:{self.specie} mancacios'


class DomesticAnimal(Animal):
    def __init__(self, age, specie, owner):
        super().__init__(age, specie)
        self.owner = owner


class WildAnimal(Animal):
    def __init__(self, age, specie, location):
        super().__init__(age, specie)
        self.location = location


def animals_eat(animals):
    for a in animals:
        print(a.eat())


animals_eat([
    DomesticAnimal(5, 'Vaca', 'Ion'),
    DomesticAnimal(4, 'Caine', 'Ion'),
    WildAnimal(25, 'Urs', 'Padure'),
    WildAnimal(40, 'Girafa', 'Jungla')
])

'''
*Polimorfismul se refera la abilitatea unui obiect de a se comporta in mai multe moduri, in functie de context.
*In esenta polimorfismul permite obiectele de acelasi tip sa aiba comportamente diferite, fara a fi necesar sa se stie tipul lor
inainte de executie
'''
