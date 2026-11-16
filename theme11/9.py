class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @property
    def is_positive(self):
        return self._balance > 0


account = BankAccount(1000)

print(account.balance)
# account.balance = 500
print(account.is_positive)
