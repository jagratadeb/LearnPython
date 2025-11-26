def welcome():
    return "Welcome!"

print(welcome())
wel = welcome
print(wel())
del welcome
print(wel())