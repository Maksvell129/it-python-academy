text = "Привет, Python! 🚀"

with open("hello.txt", "w", encoding="utf-8") as file:
    file.write(text)


with open("hello.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
