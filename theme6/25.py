

# 5**5
#
#
# 5**1 * 5**2 * 5**3 * 5**4
#
#
# !5
# 1 * 2 * 3 * 4 * 5


def sum_i(n: int) -> int:
    # 1. Базовый случай: факториал 0 или 1 равен 1
    print(f"Сейчас будем считать {n} * !{n-1}")

    if n <= 1:
        return 1

    # 2. Шаг рекурсии: n! = n * (n - 1)!
    step_result = sum_i(n-1)

    return n + step_result


# print(sum_i(5))


def infinite_recursion():
    return infinite_recursion()

infinite_recursion()