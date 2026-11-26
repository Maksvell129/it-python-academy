from theme12.exceptions import InsufficientFundsError

try:
    raise InsufficientFundsError(balance=1000,amount=1500)

except InsufficientFundsError as error:
    print(error)
    print(f"Баланс: {error.balance}")
    print(f"Запрошено: {error.amount}")
    print(f"Код ошибки: {error.status_code}")
