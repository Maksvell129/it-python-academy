class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit) -> "Temperature":
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @staticmethod
    def is_freezing(celsius: float):
        return celsius <= 0


temp1 = Temperature(celsius=-20)

print(temp1.to_fahrenheit())

temp2 = Temperature.from_fahrenheit(68)
print(temp2.celsius)

print(Temperature.is_freezing(temp1.celsius))