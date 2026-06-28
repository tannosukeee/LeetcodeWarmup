def remove_duplicates(nums):
    no_dups = []
    for num in nums:
        if num not in no_dups:
            no_dups.append(num)
    
    return no_dups

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))