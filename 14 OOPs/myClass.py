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