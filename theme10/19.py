import re

# text = "Python is great"

# result = re.search("Python", text)
#
# print(result)
# print(re.search(r"\d+", "Возраст: 25333 hdhdh"))

# text = "Цена: 100, скидка: 20, итог: 80"
#
# numbers = re.findall(
#     r"\d?", text
# )

# print(numbers)

print(re.findall(r"\d{2,4}", "123 45 789 10001 1"))