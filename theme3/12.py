# sentence = "Python это прекрасный язык"
# words = sentence.split()
# print(words)

# Разделение по конкретному символу
csv_data = "Иванов, 35, Москва, Инженер"
user_profile = csv_data.split(", ")
print(user_profile)


a = " - ".join(["Minsk", "Brest", str(123)])

print(a)