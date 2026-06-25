def group_by_frequency(lst):
    result = {}
    count = 0
    for str in lst:
        if str not in result:
            result[str] = 1
        else:
            result[str] += 1
    
    result_freq = {}
    for key in result:
        freq = result[key]

        if freq not in result_freq:
            result_freq[freq] = []
        
        result_freq[freq].append(key)
    
    return result_freq

lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))