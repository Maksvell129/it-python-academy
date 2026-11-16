import csv

users = [
    ["Alex", 25, "Minsk"],
    ["Maria", 31, "Vilnius"],
    ["John", 28, "Moscow"]
]

with open("users.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "city"])
    writer.writerows(users)

user_dicts = [
    {'name': 'Alex', 'age': '25', 'city': 'Minsk'},
    {'name': 'Maria', 'age': '31', 'city': 'Vilnius'},
    {'name': 'John', 'age': '28', 'city': 'Moscow'},
]

with open("users.csv", "w", encoding="utf-8", newline="") as file:
    fieldnames = ["name", "age", "city"]

    writer = csv.DictWriter(
        file, fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(user_dicts)
