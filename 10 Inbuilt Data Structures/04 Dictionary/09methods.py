my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
copied_dict = my_dict.copy()  # Copy dictionary
print(copied_dict)

my_dict = {"name": "Alice", "age": 25}
new_data = {"salary": 5000, "age": 28}
my_dict.update(new_data)  # Merge dictionaries
print(my_dict)
