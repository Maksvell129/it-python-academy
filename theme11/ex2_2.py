class Transport:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        if value < 0:
            print("эээ не туда летишь")
            return
        self.speed += value
        print(f"улетел на {value}")

    def brake(self, value):
        if value < 0:
            print("эээ не туда летишь")
            return

        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        print(f"отрицательный газ на {value}")

    def show_info(self):
        print(f"Корыто: {self.brand} {self.model}, скорость: {self.speed}")


class Car(Transport):
    def __init__(self, brand, model, speed=0, price=10000):
        super().__init__(brand, model, speed)
        self.price = price

    def show_info(self):
        print(f"Корыто: {self.brand} {self.model}, скорость: {self.speed} , цена : {self.price}")


class Motorcycle(Transport):
    def __init__(self, brand, model, speed=0, discount=25):
        super().__init__(brand, model, speed)
        self.discount = discount

    def show_info(self):
        print(f"Корыто на 2 колесах: {self.brand} {self.model}, скорость: {self.speed} км/ч, скидка : {self.discount}")
