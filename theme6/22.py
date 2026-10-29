def create_registration_log(ip, country):
    """
    Create registration log
    :param ip:
    :param country:
    :return:
    """
    print(f"{ip=}, {country=}")


def create_user(username, isAdmin, **kwargs):
    """создает пользователя и вызывает создание лога регистрации (см. https::)"""
    print(f"{username=}, {isAdmin=}")

    create_registration_log(**kwargs) # country="PLN", ip="127.0.0.0"


# create_user(username="alex", isAdmin=True, ip="127.0.0.0", country="PLN")




# help(create_user)
help(create_registration_log.__doc__)
