def create_registration_log(ip, country):
    print(f"{ip=}, {country=}")


def create_user(username, isAdmin, **kwargs):
    print(f"{username=}, {isAdmin=}")

    create_registration_log(**kwargs) # country="PLN", ip="127.0.0.0"


create_user(username="alex", isAdmin=True, ip="127.0.0.0", country="PLN")

