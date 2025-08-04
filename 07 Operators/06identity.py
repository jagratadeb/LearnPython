# Identity Operators in Python
a = "Hello"
b = "Hello"
print(f"a is b: {a is b}")       # True (same object in memory)

p = 10
q = 10
print(f"p is q: {p is q}")       # True (same value, same object in memory)


# Defining two lists
x = [1, 2, 3]
y = [1, 2, 3]

# Checking object identity
print(f"x is y: {x is y}")       # False (different objects in memory)
print(f"x is not y: {x is not y}") # True (they are not the same object)

# Verifying with identical assignment
z = x  # z points to the same object as x
print(f"x is z: {x is z}")       # True (same memory reference)
