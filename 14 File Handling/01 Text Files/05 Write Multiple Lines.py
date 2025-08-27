lines = ["This is the 1st line","This is the 2nd line","This is the 3rd line","This is the 4th line"]

with open("example3.txt", "a") as file:
    for line in lines:
        file.write(line + "\n")
    