numbers = [1,2,3,4,5,6,7,8,9,10]
reverseNumber = numbers.copy()
reverseNumber.reverse()

addition = list(map(lambda x,y: x+y, numbers, reverseNumber))

print("Original :", numbers)
print("Reversed :", reverseNumber)
print(f"Addition : {addition}")