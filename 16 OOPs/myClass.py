# Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

    def start_engine(self):
        print(f"The engine of {self.make} {self.model} is now running.")

    def drive_car(self):
        print(f"The {self.make} {self.model} is now driving.")
    
    def stop_car(self):
        print(f"The {self.make} {self.model} has stopped.")

# Student class
class Student:
    class_year = 2025 # class variable

    def __init__(self,name, age):
        self.name = name
        self.age = age

# Animal class
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Dog class inherited from Animal
class Dog(Animal):
    pass
# Cat class inherited from Animal
class Cat(Animal):
    pass



class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass