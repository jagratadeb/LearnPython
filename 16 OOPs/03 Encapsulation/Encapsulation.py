class Student:
    def __init__(self, name, age):
        # Public variable → can be accessed anywhere
        self.name = name
        
        # Protected variable → meant for internal use, accessible in class & subclasses
        self._age = age
        
        # Private variable → hidden from outside, only accessible inside the class
        self.__grade = None

    # Getter → used to safely access private data
    def get_grade(self):
        return self.__grade

    # Setter → used to safely update private data
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100.")

    # Public method → shows student info
    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}, Grade: {self.__grade}")


# -------------------------------
# Example usage
# -------------------------------
student = Student("Jagrata", 21)

print(student.name)        # Public → works fine
print(student._age)        # Protected → works, but not recommended
# print(student.__grade)   # Private → won't work

student.set_grade(95)      # Setter → safely set grade
print(student.get_grade()) # Getter → safely get grade
student.display_info()
