def generate_numbers(limit):
    for number in range(limit):
        yield number


# for number in generate_numbers(5):
#     print(number)

# generator = generate_numbers(3)
#
# print(next(generator))
# print(next(generator))
# print(next(generator))

numbers = (x for x in range(1_000_000))

print(type(numbers))

for n in numbers:
    print(n)

print("++++++++++")
for n in numbers:
    print(n)