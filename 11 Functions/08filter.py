def even(num):
    if (num % 2 == 0):
        return num
    
def odd(num):
    if(num % 2 != 0):
        return num
    
numbers = [1,2,3,4,5,6,7,8,9,10]

even_list = list(filter(even,numbers))
odd_list = list(filter(odd,numbers))

print(f"Odd List: {odd_list}")
print(f"Even List: {even_list}")


def get_details(person):
    return person['age'] > 25
people = [
    {'name':'Jagrata', 'age': 20},
    {'name':'Human', 'age':30}
]
print(list(filter(get_details, people)))
