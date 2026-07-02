def contains_nearby_duplicate(lst, k):
    for i in range(len(lst)):
        if i < len(lst) - k and lst[i] == lst[i + k]:
            return True
    
    return False

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))