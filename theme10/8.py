numbers = []

with open("numbers.txt", encoding="utf-8") as file:
    for line in file:
        numbers.append(int(line.strip()))

print(numbers)

