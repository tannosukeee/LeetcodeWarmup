def num_identical_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                count += 1
    
    return count

nums = [1,2,3,1,1,3]
print(num_identical_pairs(nums))

nums = [1,2,3]
print(num_identical_pairs(nums))

nums = [1,1,1,1]
print(num_identical_pairs(nums))