def multiply_list(lst, multiplier):
    result = []
    for num in lst:
        result.append(num * multiplier)
    
    return result

lst = [1,2,3]
new_lst = multiply_list(lst, 3)
print(new_lst)