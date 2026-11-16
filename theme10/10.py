
lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("languages.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
