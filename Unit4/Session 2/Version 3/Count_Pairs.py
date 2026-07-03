def count_pairs(nums, target):
	count = 0
	n = len(nums)
	i = 0
	j = 1
	while i < n:
		if j >= n:
			i += 1
			j = i + 1
		elif nums[i] + nums[j] < target:
			count += 1
			j += 1
		else:
			j += 1
	return count
		

nums = [-1,1,2,3,1]
print(count_pairs(nums,2))

nums2 = [-6,2,5,-2,-7,-1,3]
print(count_pairs(nums2,2))