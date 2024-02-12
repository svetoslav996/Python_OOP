from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, fuel_quantity, fuel_consuption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consuption = fuel_consuption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consuption + 0.9)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consuption + 1.6)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
