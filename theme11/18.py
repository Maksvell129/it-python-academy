class Engine:
    def start(self):
        print("Двигатель запущен")

class Heat:
    def start(self):
        print("Обогрев запущен")


class AC:
    def start(self):
        print("Кондиционер запущен")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.heat = Heat()
        self.AC = AC()

    def start(self):
        self.engine.start()
        self.heat.start()
        self.AC.start()



bmw = Car()
print(bmw)
print(bmw.engine)
bmw.start()