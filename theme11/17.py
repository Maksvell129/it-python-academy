from theme11.mixins import LogMixin, JsonMixin


class User(LogMixin, JsonMixin):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_banned = False

    def create(self):
        self.log("Пользователь создан")


    def ban(self, reason: str):
        self.is_banned = True
        self.log(f"Пользователь забанен {reason}")


    def send_mail(self, text:str):
        # отпрвка
        self.log(f"Отправлено письмо пользователем {self.username}")



class Product(LogMixin, JsonMixin):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def create(self):
        self.log("Продукт создан")

    def apply_discount(self, percent: int):
        # отпрвка
        self.log(f"Применена скидка к товару {self.name} в размере {percent}%")
        self.price = self.price * (1 - percent/100)

user = User("Alex123", "qwerty")

user.create()

user.send_mail("Hello")
user.ban("Мошенник")

pr = Product("Milk", 100)
pr.create()
pr.apply_discount(2)
pr.apply_discount(3)


print(user.to_json())
print(pr.to_json())