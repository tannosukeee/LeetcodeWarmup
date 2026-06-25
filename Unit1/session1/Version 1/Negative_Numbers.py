def print_negatives(lst):
    count = 0
    for i in lst:
        if i < 0:
            print(i)
            count += 1
    
    if count == 0:
        print("None")

print_negatives([3,-2,2,1,-5])
print_negatives([1,2,3,4,5])