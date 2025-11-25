try:
    file = open('example.txt','r')
    data = file.read()
except FileNotFoundError:
    print("The file does not exist.")
else:
    print("File read successfully...\n")
    print(data)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")


