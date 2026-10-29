def check_password(password: str) -> bool:
    if len(password) < 8:
        return False

    has_digit = False
    has_upper = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char in "!@#$%":
            has_special = True

    if has_digit and has_upper and has_special:
        return True
    else:
        return False


# print(check_password("pass1!#"))
# print(check_password("password1"))
# print(check_password("Password1%"))
# print(check_password("P1!@#$%!@#$%"))



def check_password(password: str) -> bool:

    if len(password) < 8:
        return False

    has_digit = False
    has_upper = False
    has_special = False

    for char in password:
        if char in "0123456789":
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char in "!@#$%":
            has_special = True

    if not has_digit or not has_upper or not has_special:
        return False

    return True
