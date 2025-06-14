# Taking user input and handling different data types

# String input
name = input("Enter your name: ")  # Default input is always a string
print(f"Hello, {name}! Welcome to Python.")

# Integer input (converted using int())
age = int(input("Enter your age: "))  
print(f"You are {age} years old.")

# Float input (converted using float())
height = float(input("Enter your height in meters: "))  
print(f"Your height is {height} meters.")

# Printing all collected inputs
print(f"\nSummary:\nName: {name}\nAge: {age}\nHeight: {height}m")
