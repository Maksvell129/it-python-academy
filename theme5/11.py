total_sum = 0

while True:
    num = int(input("Введите число: "))

    if num < 0:
        break
    else:
        total_sum += num

print(total_sum)