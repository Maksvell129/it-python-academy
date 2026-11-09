try:
    1 + "l"

    int("ppp")

except ValueError:
    print("Некорректное значение")
except TypeError:
    print("Некорректное значение")
except ZeroDivisionError:
    print("Некорректное значение")
except Exception:
    print("Другая ошибка")

