def sum_positive_range(stop):
    num = 0
    for i in range(1, stop + 1):
        num += i
    
    return num

print(sum_positive_range(6))