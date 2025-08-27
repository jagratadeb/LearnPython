data = b"This is binary data."

with open("example_binary.bin", "wb") as file:
    file.write(data)