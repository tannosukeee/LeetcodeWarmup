def find_majority_element(elements):
    result = {}
    for num in elements:
        if num not in result:
            result[num] = 1
        else:
            result[num] += 1
    
    max = 0
    e = 0
    for key in result:
        if result[key] > max:
            max = result[key]
            e = key
    
    n = len(elements) / 2
    if max > n:
        return e
    else:
        return None

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))