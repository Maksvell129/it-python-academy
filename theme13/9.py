def numbers():
    number = 1

    while True:
        yield number
        number += 1

generator = numbers()

print(next(generator))
print(next(generator))

for number in generator:
    print(number)
