def count_zeroes(lst):
    if lst[0] == 1:
        return 0
    elif lst[0] == 0:
        return 1 + count_zeroes(lst[1:])

print(count_zeroes([0, 0, 0, 1, 1, 1, 1]))
