# Creating a list
my_list = [1, 2, 3, 4, 5, 99]
print(my_list)

# Modifying elements
my_list[2] = 10  # Change element at index 2
print(my_list)

# Adding elements
my_list.append(6)  # Append element
my_list.insert(2, 99)  # Insert at index 2
my_list.extend([7, 8, 9])  # Extend list
print(my_list)

# Removing elements
my_list.remove(99)  # Remove specific element
popped_value = my_list.pop(2)  # Pop at index 2
del my_list[0]  # Delete element at index 0
print(my_list)

