# Loops in Python
# for loop
for i in range(5):
    print("for loop iteration:", i)

# while loop
count = 0
while count < 3:
    print("while loop count:", count)
    count += 1

# Nested loops
for i in range(2):
    for j in range(2):
        print(f"Nested loop: i={i}, j={j}")

# break statement
for i in range(5):
    if i == 3:
        break
    print("Break at:", i)

# continue statement
for i in range(5):
    if i == 2:
        continue
    print("Continue at:", i)

# pass statement
for i in range(3):
    pass  # Does nothing

# else with loops
for i in range(3):
    print(i)
else:
    print("Loop finished without break")
