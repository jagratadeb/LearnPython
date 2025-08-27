import random

print(random.randint(1, 100)) # Generates a random integer between 1 and 100
print(random.random()) # Generates a random float between 0.0 and 1.0
print(random.choice(['apple', 'banana', 'cherry'])) # Randomly selects an element from a list
print(random.sample(range(1, 101), 5)) # Randomly selects 5 unique elements from a range from 1 to 100
print(random.uniform(1.0, 10.0)) # Generates a random float between 1.0 and 10.0