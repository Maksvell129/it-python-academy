class BankError(Exception):

    def _translate_message(self, message: str) -> str:
        # перевод текста ошибки


        return message


class InsufficientFundsError(BankError):
    status_code = 500
    message = "Недостаточно средств: баланс {balance}, запрошено {amount}"

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        # перевод текста ошибки

        message = self._translate_message(self.message)

        super().__init__(message.format(balance=self.balance, amount=self.amount))


class InvalidAmountError(BankError):
    pass
