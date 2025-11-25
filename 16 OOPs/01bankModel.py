class BankAccount:
    # constructor
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} Deposited! New Balance: {self.balance}")
        else:
            print(f"Cannot deposit Rs.{amount}!")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"New Balance: {self.balance}")
        else:
            print(f"Insufficient balance!")

    def checkBalance(self):
        return self.balance


account = BankAccount("Jagrata",1000)
print(account.checkBalance())
account.deposit(2000)
account.withdraw(4000)
account.withdraw(2500)
print(account.checkBalance())
