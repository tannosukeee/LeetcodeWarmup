def create_dictionary(keys, values):
    if len(keys) != len(values):
        return None
    
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    
    return result

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))