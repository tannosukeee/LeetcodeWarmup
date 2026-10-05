def binary_search(nums, target):
    def helper(l, r):
        m = (l + r) // 2
        if l > r:
            return m

        if nums[m] == target:
            return m
        elif nums[m] < target:
            return helper(m + 1, r)
        else:
            return helper(l, m - 1)
    return helper(0, len(nums) - 1)

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(nums, target))
