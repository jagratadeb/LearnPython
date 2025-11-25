from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine has started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine has started"

def start_vehicle(vehicle):
    return vehicle.start_engine()

car = Car()
motorcycle = Motorcycle()

print(start_vehicle(car))
print(start_vehicle(motorcycle))
    
