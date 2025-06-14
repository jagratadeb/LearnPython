# Identity Operators in Python

# Defining two lists
x = [1, 2, 3]
y = [1, 2, 3]

# Checking object identity
print(f"x is y: {x is y}")       # False (different objects in memory)
print(f"x is not y: {x is not y}") # True (they are not the same object)

# Verifying with identical assignment
z = x  # z points to the same object as x
print(f"x is z: {x is z}")       # True (same memory reference)
