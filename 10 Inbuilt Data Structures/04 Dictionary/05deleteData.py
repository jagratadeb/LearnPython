my_dict = {"name": "Alice", "age": 25, "city": "New York"}
del my_dict["city"]  # Delete a key-value pair
print(my_dict)

removed_value = my_dict.pop("age")  # Remove and return a value
print("Removed:", removed_value)
print(my_dict)

my_dict.clear()  # Remove all elements
print(my_dict)
