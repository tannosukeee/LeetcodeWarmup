def increment_values(lst):
    result = []
    for num in lst:
        result.append(num + 1)
    
    return result

lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)