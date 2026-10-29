def multiply_string(text: str, count: int) -> str:
    return text * count

# Аннотирование обычных переменных
user_age: int = 25
is_active: bool = True
price: float = 199.99
name: str = "Alex"

print(multiply_string(name, name))

print(multiply_string(user_age, 4))
print(multiply_string(is_active, 5))