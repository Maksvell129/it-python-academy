is_admin = True
is_two_factor_auth = False
is_phone_verified = False

if is_admin:
    print("Доступ в админ-панель...")

    if is_two_factor_auth:
        print("Вход успешно выполнен!")
    else:
        print("Ошибка! Подтвердите вход по SMS.")

        if is_phone_verified:
            print("Смс отправлено вам на телефон.")
        else:
            print("Вход запрещён. Свяжитесь с главным администратором.")


else:
    print("У вас нет прав администратора.")

