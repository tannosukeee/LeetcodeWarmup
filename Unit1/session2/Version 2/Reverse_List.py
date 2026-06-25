def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)