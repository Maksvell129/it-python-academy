import re

text = "Мой номер: 123456"

result = re.sub(r"\d", "*", text)

print(result)


# 1.1.23.4

example = r"\d.\d.\d+.\d{4}"

a = r"https?:\/\/[^\s/$.?#].[^\s]*"
b = r"\b(?:https?:\/\/)?(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+(?:\/[^\s]*)?"