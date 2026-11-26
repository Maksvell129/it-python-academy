class OrderError(Exception):
    pass


class InvalidOrderStateError(OrderError):
    pass


class Order:
    def __init__(self, id: int, amount: float, currency: str = "EUR", status: str = "created"):
        self.id = id
        self.amount = amount
        self.currency = currency
        self._status = status

    @property
    def status(self) -> str:
        return self._status

    def pay(self):
        if self._status == "payed":
            raise InvalidOrderStateError(f"Заказ {self.id} уже оплачен")

        if self.status == 'cancelled':
            raise InvalidOrderStateError(f'Нельзя оплатить отмененный заказ #{self.id}.')

        self._status = "payed"

    def cancel(self):
        if self._status == "payed":
            raise InvalidOrderStateError(f"Нельзя отменить оплаченный заказ {self.id}")

        if self.status == "cancelled":
            raise InvalidOrderStateError(f"Заказ #{self.id} уже отменён.")

        self._status = "cancelled"

    def __str__(self) -> str:
        return (
            f"Заказ #{self.id}: {self.amount} {self.currency}, "
            f"статус: {self._status}"
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Order):
            return NotImplemented

        return self.id == other.id


o1 = Order(1001, 250)
print(o1)

o1.pay()
print(o1)

try:
    o1.cancel()
except InvalidOrderStateError as ex:
    print("Ошибка:", ex)

o2 = Order(1001, 250)
o3 = Order(1003, 250)

print(o1 == o2)
print(o1 == o3)
