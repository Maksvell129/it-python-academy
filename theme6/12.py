def info(name, age, **kwargs):
    print(name, age)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# numbers = [10, 20]
# print(*numbers) # print(10, 20)

person = {
    "name": "Иван",
    "age": 25,
    "money": 100
}

info(name=person["name"], age=person["age"])
info(**person) # info(name="Иван", age=25, money=100)

#
# info(name="Иван", age=25)

