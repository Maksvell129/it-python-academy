import random


is_include_negative = True

number = random.randint(-10 if is_include_negative else 0,10)

print(number)


if is_include_negative:
    number = random.randint(-10,10)
else:
    number = random.randint(0,10)

print(number)