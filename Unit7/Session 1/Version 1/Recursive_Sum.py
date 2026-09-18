def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[len(lst) - 1] + sum_list(lst[: len(lst) - 1])

print(sum_list([1, 2, 3, 4, 5]))