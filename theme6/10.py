def sum_all_numbers(*args):
    # total = 0
    # for number in args:
    #     total += number
    # return total

    return sum(args)


print(sum_all_numbers(1, 2, 3, True))
print(sum_all_numbers(10, 20, 30, 40))
