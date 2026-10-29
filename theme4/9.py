has_ticket = False
has_passport = True
is_vip = False

# if has_ticket and has_passport:
#     print("Посадка разрешена")

# if has_ticket & has_passport:
#     print("Посадка разрешена")
#
# if has_ticket | is_vip:
#     print("Проходите в зал ожидания")

# if has_ticket or is_vip:
#     print("Проходите в зал ожидания")


if ((not has_ticket) and not has_passport and not is_vip or (not has_ticket and has_passport) and
        (not has_ticket) and not has_passport and not is_vip or (not has_ticket and has_passport)):
    print("Внимание! Вы забыли билет!")