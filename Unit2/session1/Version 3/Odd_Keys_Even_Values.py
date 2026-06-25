def odd_keys_even_values(dictionary):
    result = []
    for key in dictionary:
        if key % 2 != 0 and dictionary[key] % 2 == 0:
            result.append(key)
    
    return result

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)