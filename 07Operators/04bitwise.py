# Bitwise Operators in Python

# Defining two numbers
x = 10  # Binary: 1010
y = 4   # Binary: 0100

# Performing bitwise operations
print(f"Bitwise AND: {x} & {y} = {x & y}")   # 1010 & 0100 → 0000 (0)
print(f"Bitwise OR: {x} | {y} = {x | y}")    # 1010 | 0100 → 1110 (14)
print(f"Bitwise XOR: {x} ^ {y} = {x ^ y}")   # 1010 ^ 0100 → 1110 (14)
print(f"Bitwise NOT: ~{x} = {~x}")           # Inverts all bits (~1010 → -11 in two's complement)
print(f"Right Shift: {x} >> 2 = {x >> 2}")   # 1010 >> 2 → 0010 (2)
print(f"Left Shift: {x} << 2 = {x << 2}")    # 1010 << 2 → 101000 (40)
