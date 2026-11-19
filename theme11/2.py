class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Привет, я {self.name}")

    def have_birthday(self):
        self.age += 1

    def get_info(self):
        print(f"Я {self.name}, мне {self.age}")



user1 = User("Alex", 25)
user2 = User("Maria", 30)

user1.get_info()
# user2.get_info()
user1.have_birthday()
# user2.have_birthday()
user1.get_info()
# user2.get_info()

user1.age = 9999
user1.get_info()

