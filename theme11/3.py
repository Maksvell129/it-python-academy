
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount


account_1 = BankAccount(100)
print(account_1.balance)
account_1.deposit(100)
print(account_1.balance)
account_1.withdraw(150)
print(account_1.balance)

# account_1.balance = -10000

# print(account_1.balance)