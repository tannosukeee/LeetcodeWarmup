def find_last(lst, target):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if lst[mid] == target:
            if target in lst[mid + 1 : right]:
                left = mid + 1
            else:
                return mid
        elif lst[mid] < target:
            left = mid
        else:
            right = mid
    return -1

lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
target = 11
print(find_last(lst, target))