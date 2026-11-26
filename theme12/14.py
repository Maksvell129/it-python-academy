class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Недостаточно средств на счёте")

        self.balance -= amount



account = BankAccount(100)

try:
    account.withdraw(101)
except InsufficientFundsError as e:
    print("Ошибка: ", e)