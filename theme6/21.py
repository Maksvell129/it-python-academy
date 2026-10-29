from theme6.constants import DEFAULT_CURRENCY


def get_currency():
    return DEFAULT_CURRENCY


def calc():
    print(DEFAULT_CURRENCY)


def format(money):
    return f"{money:.2f} {DEFAULT_CURRENCY}"

res1 = format(100.12002)
res2 = format(100999.1232313)
print(res1)
print(res2, res1)