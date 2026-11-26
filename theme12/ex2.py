from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float


    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x)**2 + (self.y-other.y)**2) ** 0.5

    @classmethod
    def origin(cls):
        return cls(0.0, 0.0)



zero = Point.origin()

point = Point(3, 4)

print(point.distance_to(zero))

