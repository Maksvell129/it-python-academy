x = 10
y = 25
user_name = "dmitry"

# Старый ленивый способ:
print("x =", x, "y =", y)

# Современный профессиональный дебаг:
print(f"{x=}, {y=}")

# # Работа с выражениями и методами:
print(f"{x + y=}")         # Выведет: x + y=35
print(f"{user_name.upper()=}")  # Выведет: user_name.upper()='DMITRY'
