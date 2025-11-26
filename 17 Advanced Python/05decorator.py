# Step 1: Define a decorator
def my_decorator(func):
    def wrapper():
        print("Before the function runs...")
        func()   # call the original function
        print("After the function runs...")
    return wrapper

# Step 2: Use the decorator
@my_decorator
# shorthand for [say_hello = my_decorator(say_hello)]
def say_hello():
    print("Hello!")

# Step 3: Call the decorated function
say_hello()
