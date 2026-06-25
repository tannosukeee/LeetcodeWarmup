def doubled(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    
    return result

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)