from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str
    price: float
    quantity: int = 0

    marks: list[str] = Field(default_factory=list)



pr = Product(name="MIlk", price=12.3, quantity=10)
pr2 = Product(name="Bread", price=1.3,  quantity=20)

print(pr)
print(pr2)