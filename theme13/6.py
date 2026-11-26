


def get_numbers():
    return [1, 2, 3]


def get_numbers2():
    yield 1
    yield 2
    yield 3



numbers = get_numbers2()

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))


