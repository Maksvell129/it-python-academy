class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)



cart1 = ShoppingCart()
cart1.add("Milk")
cart1.add("Bread")

# print(cart1)
print(len(cart1))

