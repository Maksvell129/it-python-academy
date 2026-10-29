name = "Анна"
age = 20

# Сумма
# print("Привет, меня зовут " + name + ", мне " + str(age) + " лет")

# 1-е поколение (%)
# print("Привет, меня зовут %s, мне %d лет %d" % (name, age, 333))


# 2-е поколение (.format)
welcoming_str = "Привет, меня зовут {}, мне {} лет {}"
print(welcoming_str.format(name, age, "Minsk"))
print(welcoming_str.format("Maria", "22", "Brest"))

# 3-е поколение (f-strings)
print(f"Привет, меня зовут {name}, мне {age} лет {"Minsk"}")
print(f"Привет, меня зовут {"Maria"}, мне {22} лет {"Brest"}")