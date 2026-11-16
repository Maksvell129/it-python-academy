# Создайте класс Product, который содержит информацию о товаре: название, цена, количество на складе.
# Реализуйте методы для изменения количества и получения общей стоимости товаров.
#
#     Создайте несколько товаров и рассчитайте общую стоимость инвентаря
#     Добавьте метод для применения скидки к товару
#     Реализуйте функцию поиска самого дорогого товара из списка объектов Product

class Product:
    def __init__(self, name: str, price: float, count: int):

        self.__name = name
        self.__price = price
        self.__count = count

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Цена должна быть положительной")
        self.__price = value

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, value: int):
        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.__count = value


    @property
    def total_price(self) -> float:
        return self.__price * self.__count


    def apply_discount(self, percent: int) :
        if not 0 <= percent <= 100:
            raise ValueError("Скидка должна быть от 0 до 100%")

        self.__price = round(self.price * (1 - percent / 100), 2)



def get_most_expensive_product(products: list[Product]) -> Product | None:
    if not products:
        return None

    # 1

    # most_expensive_product = products[0]
    #
    # for product in products:
    #     if product.price > most_expensive_product.price:
    #         most_expensive_product = product
    #
    # return most_expensive_product

    # 2
    return max(products, key=lambda p: p.price)


def get_total_remaining_price(products: list[Product]) -> float:
    summ = 0
    for product in products:
        summ += product.total_price

    return summ


milk = Product("Milk", price=5.00, count=3)
bread = Product("Bread", price=2.00, count=3)
ice_cream = Product("Ice cream", price=3.00, count=3)
cereal = Product("Cereal", price=10.00, count=3)


print(get_total_remaining_price([milk, bread]))

milk.apply_discount(20)

print(get_total_remaining_price([milk, bread]))

most_expensive = get_most_expensive_product([milk, bread, ice_cream, cereal])
print(most_expensive.name, most_expensive.price)