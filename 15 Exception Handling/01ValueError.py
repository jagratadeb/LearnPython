try:
    a = b
except NameError as e:
    print("Variable not assigned.")
    print(e)