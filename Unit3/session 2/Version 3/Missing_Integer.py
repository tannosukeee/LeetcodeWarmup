def find_missing_positive(nums):
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            return nums[i - 1] + 1
    
    return nums[len(nums) - 1] + 1

nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))