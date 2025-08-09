text = "  Hello, Python World! 123 "

# Case conversion
print("Uppercase:", text.upper()) # '  HELLO, PYTHON WORLD! 123 '
print("Lowercase:", text.lower()) # '  hello, python world! 123 '
print("Title Case:", text.title()) # '  Hello, Python World! 123 '
print("Swap Case:", text.swapcase()) # '  hELLO, pYTHON wORLD! 123 '
print("Capitalized:", text.capitalize()) # '  Hello, python world! 123 '

# Whitespace trimming
print("Stripped:", text.strip()) # 'Hello, Python World! 123'
print("Left Strip:", text.lstrip()) # 'Hello, Python World! 123 '
print("Right Strip:", text.rstrip()) # '  Hello, Python World! 123'

# Searching and counting
print("Count of 'o':", text.count('o')) # 3
print("Find 'Python':", text.find('Python')) # 8
print("Index of 'World':", text.index('World')) # 15

# Validation checks
print("Is Alphanumeric:", text.isalnum()) # False
print("Is Alphabetic:", text.isalpha()) # False
print("Is Digit:", text.isdigit()) # False
print("Is Lowercase:", text.islower()) # False
print("Is Uppercase:", text.isupper()) # False
print("Is Title:", text.istitle()) # False

# Replace and split
print("Replace 'World' with 'Universe':", text.replace('World', 'Universe')) # '  Hello, Python Universe! 123 '
print("Split by space:", text.split()) # ['  Hello,', 'Python', 'World!', '123']
print("Splitlines:", "Line1\nLine2".splitlines()) # ['Line1', 'Line2']

# Join and justify
words = ["Python", "is", "fun"] # List of words to join
print("Joined:", " ".join(words)) # 'Python is fun'
print("Centered:", text.center(40, '-')) # '----------  Hello, Python World! 123 ----------'
print("Left Justified:", text.ljust(40, '*')) # '  Hello, Python World! 123 ***************'
print("Right Justified:", text.rjust(40, '*')) # '***************  Hello, Python World! 123'

# Encoding and translation
encoded = text.encode()
print("Encoded:", encoded)

# Partitioning
print("Partition on ',':", text.partition(','))

# Tab expansion
tabbed = "Python\tis\tawesome"
print("Expanded Tabs:", tabbed.expandtabs(4))

print("Hello, my name is {} and I am learning {}".format("Jagrata", "Python"))

print("Hello, my name is {name} and I am learning {language}".format(name="Jagrata", language="Python"))