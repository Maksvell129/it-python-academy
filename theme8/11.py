def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

counter = make_counter()
print(counter())
print(counter())
print(counter())
print(counter())
print(counter.__closure__[0].cell_contents)

print("++" *10)

counter2 = make_counter()
print(counter2())
print(counter2())
print(counter2())
print(counter2())
print(counter2.__closure__[0].cell_contents)
print("++" *10)
print(counter())
print(counter())