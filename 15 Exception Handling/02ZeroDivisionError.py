try:
    result = int(10/0 )
except Exception as e:
    print("Cannot divide by 0 (zero).")
    print(e)
else:
    print(result)
