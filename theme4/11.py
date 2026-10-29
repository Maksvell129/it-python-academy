
curs = int(input("Введите ваш курс: "))


# if curs == 1:
#     print("Аудитория 101")
# elif curs == 2:
#     print("Аудитория 102")


match curs:

    case 1:
        print("Аудитория 101")

    case 2:
        print("Аудитория 102")

    case 3:
        print("Спортзал")

    case 4:
        print("Аудитория 301")

    case _:
        print("Идите домой")