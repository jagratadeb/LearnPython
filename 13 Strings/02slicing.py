# Slicing strings in Python
# Syntax: string[start:end:step]
# - start: starting index (inclusive)
# - end: ending index (exclusive)
# - step: step size (default is 1)

a = "hello" 
print(a)  # Output: hello
print(a[1:4])  # Output: ell (characters from index 1 to 3)
print(a[1:])  # Output: ello (characters from index 1 to the end)
print(a[:3])  # Output: hel (characters from the start to index 2)
print(a[1:4:2])  # Output: el (characters from index 1 to 3, stepping by 2)
print(a[::2])  # Output: hlo (every second character)
print(a[::-1])  # Output: olleh (reversed string)