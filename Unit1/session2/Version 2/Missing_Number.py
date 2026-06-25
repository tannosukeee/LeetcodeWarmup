def find_missing(nums):
    for i in range(len(nums) - 1):
        if i not in nums:
            return i
    
    return None

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)