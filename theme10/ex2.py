# with open('log.txt', 'a', encoding='utf-8') as file:
#     print("Сервер запущен!")
#     while True:
#         user_msg = input("Введите сообщение: ")
#         if not user_msg == "exit":
#             file.write(user_msg + "\n")
#         else:
#             break

while True:
    message = input("Введите сообщение: ")

    if message == "выход":
        print("Покеда.")
        break

    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")

lines = []

while True:
    message = input("Введите сообщение: ")

    if message == "выход":
        print("Покеда.")
        break

    lines.append(message)

with open("log.txt", "a", encoding="utf-8") as file:
    file.writelines(lines)