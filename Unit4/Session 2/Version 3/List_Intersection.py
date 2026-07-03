def find_intersection(lst1, lst2):
    result = []
    i = 0
    j = 0
    while i < len(lst1) or j < len(lst2):
        if lst1[i] == lst2[j]:
            result.append(lst1[i])
            i += 1
            j += 1
        else:
            if lst1[i] < lst2[j]:
                i += 1
            else:
                j += 1
    
    while i < len(lst1):
        if lst1[i] in lst2:
            result.append(lst1[i])
            i += 1
        else:
            i += 1
    
    while j < len(lst2):
        if lst2[j] in lst1:
            result.append(lst2[j])
            j += 1
        else:
            j += 1
    
    return result

lst1 = [1,2,4,6,7]
lst2 = [2,3,4,7]
print(find_intersection(lst1, lst2))