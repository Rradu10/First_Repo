class Dog:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return f'Varsta : {self.age}, Nume: {self.name}'
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        if not isinstance(other,Dog):
            return False
        return self.name==other.name
d=Dog(1,'Bolt')
print(d)
d2=Dog(2,'Sparky')
l=[d,d2]
print(l)
d3=Dog(3,'Colt')
l=[d,d2,d3]
print(l)

print(d3==d2)
print(d3==7)
