def list_product(lst):
    if len(lst) == 0:
        return 1
    else:
        return lst[len(lst) - 1] * list_product(lst[: len(lst) - 1])

lst = [1, 2, 3, 4, 5]
print(list_product(lst))
