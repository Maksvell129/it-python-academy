from dataclasses import dataclass, field


@dataclass(frozen=True)
class Point:
    x: int
    y: int


point = Point(1, 2)

point.x = 100
print(point)