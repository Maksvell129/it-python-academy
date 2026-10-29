number = int(input('Введите число: '))
is_odd = None
is_positive = None


if number % 2 == 0:
    is_odd = True

else:
    is_odd = False


is_ok = True if number % 2 == 1 else True if number > 0 else True


print(is_ok)

# if not is_odd and is_positive:
#     print("подходит")