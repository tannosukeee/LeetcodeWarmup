def interleave_lists(lst1, lst2):
    result = []
    if len(lst1) > len(lst2):
        n = len(lst1)
    else:
        n = len(lst2)
    
    for i in range(n):
        if i < len(lst1) and i < len(lst2):
            result.append(lst1[i])
            result.append(lst2[i])
    
    for e in lst1:
        if e not in result:
            result.append(e)
    
    for e in lst2:
        if e not in result:
            result.append(e)

    return result

lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst)