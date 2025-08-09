text = "  Hello, Python World! 123 "

# Case conversion
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Swap Case:", text.swapcase())
print("Capitalized:", text.capitalize())

# Whitespace trimming
print("Stripped:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())

# Searching and counting
print("Count of 'o':", text.count('o'))
print("Find 'Python':", text.find('Python'))
print("Index of 'World':", text.index('World'))

# Validation checks
print("Is Alphanumeric:", text.isalnum())
print("Is Alphabetic:", text.isalpha())
print("Is Digit:", text.isdigit())
print("Is Lowercase:", text.islower())
print("Is Uppercase:", text.isupper())
print("Is Title:", text.istitle())

# Replace and split
print("Replace 'World' with 'Universe':", text.replace('World', 'Universe'))
print("Split by space:", text.split())
print("Splitlines:", "Line1\nLine2".splitlines())

# Join and justify
words = ["Python", "is", "fun"]
print("Joined:", " ".join(words))
print("Centered:", text.center(40, '-'))
print("Left Justified:", text.ljust(40, '*'))
print("Right Justified:", text.rjust(40, '*'))

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