def count_rotations(nums):
    nums_sorted = sorted(nums)
    for i in range(len(nums_sorted)):
        if nums_sorted[i] == nums[0]:
            return i
print(count_rotations([8, 9, 10, 2, 5, 6]))
