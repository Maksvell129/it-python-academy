
# try:
    # код, в котором может возникнуть исключение
# except:
    # обработка исключения


try:
    number = int("hello")
except (ValueError, TypeError) as error:
    print(error.__doc__)
    print(str(error))
    print(type(error))

