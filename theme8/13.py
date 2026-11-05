def my_decorator(func):

    def wrapper():
        print("--- Что-то происходит ДО вызова функции ---")
        func()
        print("--- Что-то происходит ПОСЛЕ вызова функции ---")

    return wrapper


def say_hi():
    print("Привет!")

def say_bye():
    print("Пока!")


# Ручное обертывание:
say_hi_decorated = my_decorator(say_hi)
say_hi_decorated()

say_bye_decorated = my_decorator(say_bye)
say_bye_decorated()
