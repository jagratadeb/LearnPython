numbers = [1,2,3,4,5]
it = iter(numbers)

try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("End of the list reached.")