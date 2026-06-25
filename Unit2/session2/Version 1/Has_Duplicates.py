def has_duplicates(nums, k):
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] == nums[j] and (j - i) <= k:
				return True
	return False

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = has_duplicates(nums, 2)
print(check1)
check2 = has_duplicates(nums, 5)
print(check2)
check3 = has_duplicates(nums, 3)
print(check3)