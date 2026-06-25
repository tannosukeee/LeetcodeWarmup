def print_odd_indices(nums):
    for i in range(len(nums)):
        if i % 2 != 0:
            print(nums[i])

nums = [3,4,8,1,5,2]
print_odd_indices(nums)