def find_unique_items(list_a, list_b):
    result = {}
    for i in list_a:
        if i not in list_b:
            result[i] = True
    
    for i in list_b:
        if i not in list_a:
            result[i] = False
    
    return result

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))