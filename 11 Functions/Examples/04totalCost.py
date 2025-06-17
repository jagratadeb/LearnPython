def totalCost(cart):
    totalCost = 0
    for items in cart:
        totalCost += (items["price"] * items["quantity"])
    return totalCost

cart = [
    {'name':'guava','price':0.5,'quantity':5}, # 2.5
    {'name':'watermelon','price':0.4,'quantity':4}, # 1.6
    {'name':'apple','price':0.5,'quantity':3}, # 1.5
    {'name':'mango','price':0.2,'quantity':2}, # 0.4
    {'name':'banana','price':0.1,'quantity':1}, # 0.1
    # total cost = 6.1 
]

print(totalCost(cart))