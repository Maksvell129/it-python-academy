try:
    a = int(input())
    b = int(input())

    result = a / b

except ValueError:
    print("Нужно вводить числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")
