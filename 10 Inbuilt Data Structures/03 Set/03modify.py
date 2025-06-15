my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)

# Removing elements
my_set.remove(2)  # Removes an element (raises error if not found)
print(my_set)

my_set.discard(10)  # Doesn't raise error if element is absent
print(my_set)

popped_value = my_set.pop()  # Removes a random element
print(my_set)

my_set.clear()  # Removes all elements
print(my_set)

