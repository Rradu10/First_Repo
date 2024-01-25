class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def print_name(self):
        print(f'Numele meu este {self.name}')


class Student(Person):
    pass
p=Person('Adrei',27)
p.print_name()
s=Student('Maria',24)
s.print_name()

class Worker(Person):
    def __init__(self,name,age,job):
        super().__init__(name,age) # super este referinta la clasa parinte
        self.job=job
w=Worker('Ion',25,'programator')
w.print_name()
