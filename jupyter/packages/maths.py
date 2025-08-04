def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

def exponentiation(a,b):
    return a ** b

def modulus(a,b):
    return a % b

def floor_division(a,b):
    return a // b

def square_root(a):
    return a ** 0.5

def cube_root(a):
    return a ** (1/3)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
def absolute_value(a):
    if a < 0:
        return -a
    else:
        return a
    
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result