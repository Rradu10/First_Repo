class Car:
    def go(self):
        print('Vroom Vroom!')
    def start(self):
        print('Starting Car')

class Flyable:
    def fly(self):
        print('Flu Flu!')
    def start(self):
        print('Starting Flyable')

class FlyingCar(Car,Flyable):
    pass

c = FlyingCar()
c.go()
c.fly()
c.start()

#MRO - Method Resolution Order : Se decide care functie din clasa car sau flyable se va apela (de la stanga la dreapta)
