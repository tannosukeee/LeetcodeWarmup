def find_all_occurrences(lst, target):
    result = []

    for i in range (len(lst)):
        if lst[i] == target:
            result.append(i)
    
    return result

lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)