score = 10
print(id(score))  # Адрес А
score = score + 1  # Перезапись значения
print(id(score))


greeting = "Привет"
print(id(greeting))  # Адрес В
greeting += "!"
print(id(greeting))  # Адрес Г (Создана новая строка "Привет!")


score = score + 1
score += 1

score = score - 1
score -= 1 