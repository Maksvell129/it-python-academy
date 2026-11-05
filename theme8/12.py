multipliers = []

for i_iteration in range(3):
    print(f'{i_iteration=}')
    multipliers.append(lambda x: x * i_iteration)


print(multipliers[0](2))  # 0
print(multipliers[1](2))  # 1
print(multipliers[2](2))  # 2

print("==" * 10)

# РЕШЕНИЕ: Фиксация i через аргумент по умолчанию (Early Binding)
multipliers_correct = []

for i_iteration in range(3):
    print(f'{i_iteration=}')
    multipliers_correct.append(lambda x, i_lambda=i_iteration: x * i_lambda)


print(multipliers_correct[0](2))  # 0 (2 * 0)
print(multipliers_correct[1](2))  # 2 (2 * 1)
print(multipliers_correct[2](2))  # 4 (2 * 2)
