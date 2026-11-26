
from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    # marks : list[str] = []
    marks: list[str] = field(default_factory=list)


    def total_cost(self):
        return self.price * self.quantity


pr = Product("MIlk", 12.3, 10)
pr2 = Product("Bread", 1.3, 20)
print(pr)
print(pr2)

# pr.marks.append("21321321")

# print(pr.marks)
# print(pr2.marks)