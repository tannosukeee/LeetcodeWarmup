def min_merge_operations(nums):
	if nums == nums[::-1]:
		return 0
	left = 0
	right = len(nums) - 1
	count = 0
	while left < right:
		if nums[left] == nums[right]:
			left += 1
			right -= 1
		elif nums[left] < nums[right]:
			nums[left + 1] += nums[left]
			left += 1
			count += 1
		elif nums[left] > nums[right]:
			nums[right - 1] += nums[right]
			right -= 1
			count += 1
	return count

nums = [6,1,3,7]
print(min_merge_operations(nums))

nums2 = [1,3,3,1]
print(min_merge_operations(nums2))

nums3 = [1,3,2,7]
print(min_merge_operations(nums3))