


class User:
    __count = 0

    def __init__(self, name):
        self.name = name
        User.__count += 1

    @classmethod
    def show_count(cls):
        print(cls.__count)


user = User("Alex")

User.show_count()

user2 = User("Maria")


User.show_count()
