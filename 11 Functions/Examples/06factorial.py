def fact(n):
    factValue = 1
    for num in range(1, n+1):
        factValue *= num 
    return factValue


print(fact(0))
print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))