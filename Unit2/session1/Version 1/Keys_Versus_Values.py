def keys_v_values(dictionary):
    keys_sum = 0
    values_sum = 0

    for i in dictionary:
        keys_sum += i
        values_sum += dictionary[i]
    
    if keys_sum > values_sum:
        return "keys"
    elif keys_sum < values_sum:
        return "values"
    else:
        return "balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)