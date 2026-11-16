# Создадим класс товара.
#
# У товара есть:
# название;
# цена;
# количество.
#
# Цена не должна быть отрицательной.
# Поэтому мы хотим контролировать изменение price.


class Product:

    def __init__(self, name: str, price: float, count: int):
        self.__name = name
        self.__price = price
        self.__count = count

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("The price is not positive")

        self.__price = value

    @property
    def count(self):
        return self.__count

    @property
    def name(self):
        return self.__count

    def get_info(self):
        return f"{self.__name} {self.__price} {self.__count}"

    def calculate_order(self, amount: int) -> float:
        if amount > self.__count:
            raise ValueError("The amount is greater than the remaining count")

        self.__count -= amount

        return amount * self.__price

product1 = Product(name='Milk', price=10, count=3)
print(product1.get_info())
print(product1.calculate_order(2))