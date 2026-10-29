# значение_если_да if условие else значение_если_нет


number = int(input('Введите число: '))
is_odd = None

if number % 2 == 0:
    is_odd = True
else:
    is_odd = False

is_even = True if number % 2 == 1 else False

print(f"{is_odd=}")
print(f"{is_even=}")

