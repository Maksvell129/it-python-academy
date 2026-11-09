import functools
from random import randint


def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Произошла ошибка {e}. Пробуем еще раз...» и сделать вторую (повторную) попытку вызова.")
        return func(*args, **kwargs)

    return wrapper

@retry
def coinflip():
    result = randint(0, 1)

    if result:
        return "Успех"
    else:
        raise ValueError("Не повезло")


print(coinflip())

