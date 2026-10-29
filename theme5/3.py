# Синтаксис:
# while условие:
#     тело_цикла

attempts = 3

while attempts > 0:
    print(f"Попытка входа. Осталось: {attempts}")
    attempts -= 1

print("Цикл завершен.")
