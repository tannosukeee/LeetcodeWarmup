def count_ones(lst):
    l = 0
    r = len(lst) - 1
    first = 0

    while l <= r:
        m = (l + r) // 2
        if lst[m] == 0:
            l = m + 1
        elif lst[m] == 1:
            r = m - 1
            first = len(lst) - m

    return first

print(count_ones([0, 1, 1, 1, 1, 1, 1]))
