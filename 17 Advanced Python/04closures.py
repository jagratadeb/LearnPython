def welcome(msg):
    def sub_welcome_method():
        print("This is the sub method!")
        print(msg)
    return sub_welcome_method()

welcome("Welcome to Jagrata!")