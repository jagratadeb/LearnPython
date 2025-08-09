# String Methods
s = "hello world"
print(s.upper())      # 'HELLO WORLD'
print(s.capitalize()) # 'Hello world'
print(s.count('l'))   # 3
print(s.find('world'))# 6
print(s.replace('world', 'Python')) # 'hello Python'
print(s.isalpha())    # False
print("123".isdigit())# True
words = s.split()     # ['hello', 'world']
joined = '-'.join(words) # 'hello-world'
print(joined)         # 'hello-world'
