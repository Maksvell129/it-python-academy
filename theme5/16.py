

import time

# Засекаем время старта
start_time = time.time()
print(start_time)

# Выполняем тяжелый процесс
total = 0
for i in range(100_000_000):
    total += i

# Вычисляем разницу
end_time = time.time()
execution_time = end_time - start_time

print(f"Сумма посчитана за {execution_time:.4f} секунд.")


