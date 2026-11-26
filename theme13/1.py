numbers = [10, 20, 30]

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
    except StopIteration:
        break

    print(number)



for number in numbers:
    print(number)
