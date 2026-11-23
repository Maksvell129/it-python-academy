import re


pattern = r"\+\d{12}"

phone = input("Введите телефон: ")

if re.fullmatch(pattern, phone):
    print("Телефон корректен")
else:
    print("Некорректный формат")
