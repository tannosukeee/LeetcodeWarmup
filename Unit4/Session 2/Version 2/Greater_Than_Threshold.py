def num_of_subarrays(lst, k, threshold):
	i = 0
	j = k
	count = 0
	while i < len(lst) and j <= len(lst):
		total = 0
		for num in range(i, j):
			total += lst[num]
		if total / k >= threshold:
			count += 1
		i += 1
		j += 1
	return count

nums = [2,2,2,2,5,5,5,8]
count = num_of_subarrays(nums, 3, 4)
print(count)