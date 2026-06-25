def sum_even_values(dictionary):
    sum = 0

    for key in dictionary:
        if dictionary[key] % 2 == 0:
            sum += dictionary[key]
        
    return sum

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))