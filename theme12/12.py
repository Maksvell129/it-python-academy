class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __lt__(self, other):
        return self.balance < other.balance



balance1 = BankAccount(100)
balance2 = BankAccount(200)

print(balance1 < balance2) # balance1.__lt__(balance2)
print(balance1.__lt__(balance2))
