class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):

        if not type(other) == type(self):
            raise TypeError("Типы сравниваемых объектов не одинаковы")

        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Random:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(1, 2)

point2 = Point(3, 4)

point3 = Point(1, 2)

random1 = Random(1, 2)

print(point1 + point2)
# print(point1 == point3)
# print(point1 is point3)
print(point1 == random1)