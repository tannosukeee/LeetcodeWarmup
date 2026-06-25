def count_occurrences(nums):
    result = {}

    for num in nums:
        if num not in result:
            result[num] = 1
        else:
            result[num] += 1
    return result

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))