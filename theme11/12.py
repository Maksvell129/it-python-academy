from abc import ABC, abstractmethod




class Transport(ABC):

    @abstractmethod
    def move(self):
        # print("Дефолт")
        # pass
        raise NotImplementedError


class Bicycle(Transport):

    def move(self):
        print("Едем на велосипеде")


class Plane(Transport):

    def move(self):
        print("Самолёт летит")


bicycle = Bicycle()
bicycle.move()
