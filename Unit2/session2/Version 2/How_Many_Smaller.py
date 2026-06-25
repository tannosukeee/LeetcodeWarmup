def smaller_numbers_than_current(nums):
    result = []
    count = 0
    for i in range(len(nums)):
        for num in nums:
            if nums[i] > num:
                count += 1
        result.append(count)
        count = 0
    
    return result

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))