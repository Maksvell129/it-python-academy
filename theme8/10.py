def make_greeter(greeting: str):

    def greet(name: str) -> str:
        return f"{greeting}, {name}!"

    return greet


say_hello = make_greeter("Привет")
say_bye = make_greeter("До свидания")

print(say_hello("Алексей"))
print(say_hello("Максим"))
print(say_hello("Пётр"))

print(say_bye("Алексей"))
print(say_bye("Андрей"))
print(say_bye("Никита"))

print(say_hello.__closure__[0].cell_contents)
print(say_bye.__closure__[0].cell_contents)