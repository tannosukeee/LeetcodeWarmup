def exclusive_elements(lst1, lst2):
    result = []
    for num in lst1:
        if num not in lst2:
            result.append(num)
    
    for num in lst2:
        if num not in lst1:
            result.append(num)
    
    return result

lst1 = [3,1,8,10]
lst2 = [4,5,3,7,8]
excl_lst = exclusive_elements(lst1, lst2)
print(excl_lst)