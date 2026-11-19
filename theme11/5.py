class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        max_age = 160

        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")

        if value > max_age:
            raise ValueError(f"Возраст слишком большой, максимум {max_age}")

        self._age = value


user = User(33)
print(user.age)

user.age = 100
print(user.age)