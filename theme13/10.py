
def generate_numbers():
    yield 1
    yield 2

def generate_all():
    yield 3
    yield from generate_numbers()
    yield 4


for number in generate_all():
    print(number)
