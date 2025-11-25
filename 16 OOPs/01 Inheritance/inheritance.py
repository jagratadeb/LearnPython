class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print(f"The person drives the {self.enginetype} car.")

class Tesla(Car):
    def __init__(self, windows, doors, enginetype, is_selfdriving):
        super().__init__(windows, doors, enginetype)
        self.is_selfdriving = is_selfdriving

    def slefdriving(self):
        print(f"Tesla supports self driving: {self.is_selfdriving}")
        

tesla1 = Tesla(4,5,"Electric",True)
tesla1.drive()
tesla1.slefdriving()