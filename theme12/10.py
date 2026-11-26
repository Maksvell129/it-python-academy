class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r})"


user = User("Andy", 18)

print(user)


