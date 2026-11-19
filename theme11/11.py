


class Transport:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Двигатель запущен")


class Car(Transport):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def move(self):
        super().move()
        print("Автомобиль едет по трассе")


class Bus(Transport):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def move(self):
        print("Автобус двигается по маршруту")

class Motorcycle(Transport):
    def move(self):
        print("Мотоцикл соревнуется на треке")


car = Car("Toyota", "Camry", 5)
bus = Bus("MAZ", "1", 50)
moto = Motorcycle("Suzuki", "2")

# print(car, car.brand, car.model, car.doors)
# print(bus, bus.brand, bus.model, bus.seats)
# print(moto, moto.brand, moto.model)

car.move()
# bus.move()
# moto.move()

# for transport in [car, bus, moto]:
#     transport.move()

# print(isinstance(car, Car))
# print(isinstance(car, Transport))

# print(isinstance(bus, Bus))
# print(isinstance(bus, Transport))

# print(isinstance(moto, Motorcycle))
# print(isinstance(moto, Transport))

# print(isinstance(moto, Bus))
# print(isinstance(moto, Car))