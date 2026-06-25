def flip_sign(lst):
    result = []
    for num in lst:
        result.append(num * -1)
    
    return result

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)