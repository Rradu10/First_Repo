from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Vehicle:
    type: str
    capacity: int
    power: int
    owner: Person

    def ride(self):
        print(f'{self.owner.name} rides a {self.type}')


@dataclass
class UtilityVehicle(Vehicle):
    type: str = field(init=False, default='utility vehicle')
    load_capacity: int


@dataclass
class Car(Vehicle):
    type: str = field(init=False, default='car')
    fuel_type: str


@dataclass
class Bike(Vehicle):
    type: str = field(init=False, default='bike')


@dataclass
class Bus(Car):
    passengers_type: str


@dataclass
class MotorBike(Bike):
    engine_capacity: int


p1 = Person("Sergiu", 24)
p2 = Person("Valentina", 23)

VEHICLES = [
    Car(capacity=5, power=90, owner=p1, fuel_type="benzina"),
    Car(capacity=5, power=105, owner=p2, fuel_type="benzina"),
    Car(capacity=5, power=60, owner=p1, fuel_type="motorina"),
    Bus(capacity=40, power=150, owner=p2, fuel_type="motorina", passengers_type="elevi"),
    Bus(capacity=35, power=150, owner=p1, fuel_type="motorina", passengers_type="angajati"),
    Bike(capacity=1, power=5, owner=p1),
    MotorBike(capacity=1, power=80, owner=p2, engine_capacity=500),
    MotorBike(capacity=1, power=75, owner=p1, engine_capacity=250),
    UtilityVehicle(capacity=1, power=200, owner=p1, load_capacity=90),
    UtilityVehicle(capacity=1, power=150, owner=p2, load_capacity=100),
]

'''
Sa se gaseasca toate vehiculele cu capacitate de mai mult de 2 persoane
Sa se gaseana numele persoanelor care detin o Bike
Sa se gaseasca toate UtilityVehicle
'''


def find_vechicles_with_capacity_greater_than_2(vehicles):
    result = []
    for x in vehicles:
        if x.capacity > 2:
            result.append(x)
    return result


print(find_vechicles_with_capacity_greater_than_2(VEHICLES))


def find_persons_that_owns_a_bike(vehicles):
    result = set()
    for i in vehicles:
        if isinstance(i, Bike):
            result.add(i.owner.name)
    return list(result)


print(find_persons_that_owns_a_bike(VEHICLES))


def find_utility_vehicles(vehicles):
    result = []
    for x in VEHICLES:
        if isinstance(x, UtilityVehicle):
            result.append(x)
    return result


print(find_utility_vehicles(VEHICLES))
