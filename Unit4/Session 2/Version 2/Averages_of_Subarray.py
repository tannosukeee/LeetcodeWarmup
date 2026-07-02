def find_averages_of_subarrays(k, nums):
	i = 0
	j = k
	result = []
	while i < len(nums) and j <= len(nums):
		total = 0
		for num in range(i, j):
			total += nums[num]
		result.append(total / k)
		i += 1
		j += 1
	return result

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)
print(avg_lst)