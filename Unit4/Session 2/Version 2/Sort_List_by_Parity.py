def sort_array_by_parity(nums):
	i = 0
	j = 1
	while i < len(nums) and j < len(nums):
		if nums[i] % 2 == 0:
			if nums[j] % 2 != 0:
				i += 2
				j += 2
			else:
				i += 2
		elif nums[i] % 2 != 0:
			if nums[j] % 2 == 0:
				nums[i], nums[j] = nums[j], nums[i]
				i += 2
				j += 2
			else:
				j += 1
	return nums

nums = [4,2,5,7]
nums2 = [2,3]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))