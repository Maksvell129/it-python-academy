

user = {
    "username": "Alex111",
    "role": "reader",
    "is_guest": True
}


if user["role"] == "admin":
    print("Администратор")

if user["role"] == "user" and not user["is_verified"]:
    print("Доступ запрещен")

if user["role"] == "reader" or user["is_guest"]:
    print("Доступ читателю")

a = None

if a:
    print("true")
elif a is None:
    print("None")
else:
    print("false")


