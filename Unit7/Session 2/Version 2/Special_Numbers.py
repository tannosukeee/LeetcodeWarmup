def is_special(nums):
    if len(nums) == 0:
        return -1

    count = 0
    for i in range(max(nums) + 1):
        for j in range(len(nums)):
            if nums[j] >= i:
                count += 1
        if count == i:
            return count
        else:
            count = 0

    return -1

nums = [0, 0, 3, 4, 4]
print(is_special(nums))
