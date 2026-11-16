import os

if os.path.exists("data.txt"):
    with open("data.txt", "r", encoding="utf-8") as f:
        text_data = f.read()

    if not os.path.exists("backup"):
        os.mkdir("backup")

    with open("backup/data.txt", "w", encoding="utf-8") as backup:
        backup.write(text_data)

else:
    print("Ошибка: файл data.txt не найден.")



with open("data.txt", "r", encoding="utf-8") as f:

    with open("backup/data.txt", "w", encoding="utf-8") as backup:

        for line in f:
            backup.write(line)