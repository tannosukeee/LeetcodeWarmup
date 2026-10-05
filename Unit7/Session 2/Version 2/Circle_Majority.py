def search_circular_list(nums):
    mj = len(nums) // 2
    result = {}

    for n in nums:
        if n not in result:
            result[n] = 1
        else:
            result[n] += 1

    for n in result:
        if result[n] > mj:
            return n

nums = [3, 2, 3]
print(search_circular_list(nums))
