def halve_lst(lst):
    result = []
    for number in lst:
        halved = number/2
        result.append(halved)
    
    return result

print(halve_lst([2,4,6,8]))