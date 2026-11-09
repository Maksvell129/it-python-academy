def divide(a, b):
    if b == 0:
        raise ValueError("Делитель не может быть равен нулю")

    return a / b


result = divide(10, 0)
