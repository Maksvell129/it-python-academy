x = [1, 2, 3]  # Создается объект-список. Переменная x ссылается на него.
y = x
z = [1, 2, 3]

print(id(x))
print(id(y))
print(x == y)
print(x is y)
print(x == z)
print(x is z)

print(y == z)
print(y is z)

# number = 42
# print(id(number))
#
# text = "Python"
# print(id(text))
