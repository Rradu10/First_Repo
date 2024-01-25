class Dog:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def bark(self):
        print('Woof')
    def print_name(self):
        print(self.name)

d=Dog(4,'Henry')
d.bark()
d.print_name()
