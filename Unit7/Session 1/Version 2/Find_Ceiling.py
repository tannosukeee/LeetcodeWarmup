def find_ceiling(lst, x):
    left = 0
    right = len(lst) - 1
    best = -1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] >= x:
            best = mid
            right = mid - 1
        else:
            left = mid + 1
    return best

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_ceiling(lst, x))