from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

    def __str__(self):
        return(f"На балансе сейчас: {self.amount} {self.currency}")

    def __repr__(self):
        return(f"Money(amount={self.amount}, currency={self.currency})")

    def __add__(self, other):
        if self.currency == other.currency:
            return self.amount + other.amount
            # return Money(amount=self.amount + other.amount, currency=self.currency)
        else:
            raise TypeError("Невозможно сложить разные валюты")

    def __sub__(self, other):
        if self.currency == other.currency:
            return self.amount - other.amount
            # return Money(amount=self.amount - other.amount, currency=self.currency)
        else:
            raise TypeError("Невозможно вычесть разные валюты")

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency


money1 = Money(amount=10, currency="USD")
money2 = Money(amount=20, currency="EUR")
money3 = Money(amount=10, currency="USD")
money4 = Money(amount=10, currency="EUR")

print(money1 - money3)
print(money2 - money4)
print(money1 + money3)
print(money2 + money4)

print(money1 == money3)