attempts = 3

while attempts > 0:
    password = input("Пароль: ")

    if password == "python":
        print("Доступ разрешён.")
        break

    attempts -= 1
else:
    print("Все попытки закончились.")
