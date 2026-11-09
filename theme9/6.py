try:
    number = int(input())
except ValueError:
    print("Ошибка ввода")
finally:
    print("Программа завершила попытку ввода")
