def index_to_value_map(lst):
    result = {}

    for i in range(len(lst)):
        result[i] = lst[i]
    
    return result

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))