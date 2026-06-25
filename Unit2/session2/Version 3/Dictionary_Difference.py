def dict_difference(d1, d2):
    result = {}
    for key in d2:
        if key in d1:
            if d2[key] != d1[key]:
                result[key] = d2[key]
        else:
            result[key] = d2[key]
    
    return result

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d2, d1))