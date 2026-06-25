def find_min_index_of_repeating(nums):
    for i in range(len(nums)):
        if nums[i] in nums[i + 1:]:
            return i
    
    return None

nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))