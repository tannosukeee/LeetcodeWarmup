def above_threshold(lst, threshold):
    result = []
    for num in lst:
        if num > threshold:
            result.append(num)
    
    return result

lst = [8,2,13,11,4,10,14]
result = above_threshold(lst, 10)
print(result)