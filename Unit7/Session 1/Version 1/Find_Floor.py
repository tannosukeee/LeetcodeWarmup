def find_floor(lst, x):
    left = 0
    right = len(lst) - 1
    best = -1
    
    while left < right:
        mid = (left + right) // 2
        if lst[mid] <= x:
            best = mid
            left = mid + 1
        else:
            right = mid
    return best

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_floor(lst, x))