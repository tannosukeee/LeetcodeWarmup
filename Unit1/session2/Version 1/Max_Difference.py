def max_difference(lst):
    min = lst[0]
    max = lst[0]

    for num in lst:
        if num < min:
            min = num
        elif num > max:
            max = num
    
    return max - min

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)