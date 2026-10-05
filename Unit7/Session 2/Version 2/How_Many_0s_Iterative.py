def count_zeroes(lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == 1:
            right = mid - 1
        elif lst[mid] == 0:
            left = mid + 1

    return left

print(count_zeroes([0, 0, 0, 0, 1, 1, 1]))
