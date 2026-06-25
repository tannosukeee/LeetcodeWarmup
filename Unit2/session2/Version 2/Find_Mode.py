def find_mode(lst):
    count = {}
    for num in lst:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    
    max = 0
    result = []
    name = ""

    for key in count:
        if count[key] > max:
            max = count[key]
    
    for key in count:
        if count[key] == max:
            result.append(key)
    
    if len(result) > 1:
        for j in range(len(lst)):
            if lst[j] in result:
                return lst[j]
    else:
        return result[0]

lst = [1,2,3,2,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)
