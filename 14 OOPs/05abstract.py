from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("The car is moving.")

    def stop(self):
        print("The car has stopped.")

class Bicycle(Vehicle):
    def go(self):
        print("The bicycle is moving.")

    def stop(self):
        print("The bicycle has stopped.")

# Example usage

car = Car()
bicycle = Bicycle()

car.go()
car.stop()

bicycle.go()
bicycle.stop()