def find_largest_k(nums):
    if 0 in nums:
        return -1
    max = 0
    for i in range(len(nums)):
        if nums[i] > max and nums[i] * -1 in nums:
            max = nums[i]
    
    if max > 0:
        return max
    else:
        return -1

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))