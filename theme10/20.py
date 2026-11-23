import re

age = input("Введите возраст: ")

if re.fullmatch(r"\d+", age):
    print("Введено число")
else:
    print("Некорректный ввод")
