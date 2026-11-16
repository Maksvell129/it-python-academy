

class User:

    def __init__(self, name: str, age: int, email: str | None = "default@mail.com"):
        self.name = name
        self.age = age
        self.email = email


    def get_info(self):
        print("Информация о пользователе")


user1 = User(name="Alex", age=29)
user2 = User(name="Maria", age=18, email="someemail@mail.com")


print(user1.name, user1.age, user1.email)
print(user2.name, user2.age, user2.email)
