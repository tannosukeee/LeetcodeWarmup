def count_negatives(nums, k):
	i = 0
	j = k
	result = []
	count = 0
	while j <= len(nums):
		for num in range(i, j):
			if nums[num] < 0:
				count += 1
		result.append(count)
		i += 1
		j += 1
		count = 0
	return result

lst = [-1, 2, -2, 3, 5, -7, -5]
print(count_negatives(lst, 3))