def count_evens(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    
    return count

lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)