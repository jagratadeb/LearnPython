from abc import ABC, abstractmethod

# Abstraction → hide implementation, only show essential behavior
class Vehicle(ABC): 
    @abstractmethod
    def start_engine(self):
        pass   # subclasses must implement this

    @abstractmethod
    def stop_engine(self):
        pass   # subclasses must implement this


# Concrete class → provides actual implementation
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"


class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"

    def stop_engine(self):
        return "Bike engine stopped"


# Function that works with any Vehicle → abstraction in action
def operate_vehicle(vehicle):
    print(vehicle.start_engine())
    print(vehicle.stop_engine())

car = Car()
bike = Bike()

operate_vehicle(car)   # Car engine started / stopped
operate_vehicle(bike)  # Bike engine started / stopped
