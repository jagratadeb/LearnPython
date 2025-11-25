class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("the subclass will implement this")

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says woof"

dog = Dog("Buddy", "JD")
print(dog.speak())      # Buddy says woof
print(dog.owner)        # JD
