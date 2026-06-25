def remove_duplicates_from_front(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] not in nums[i + 1:]:
            result.append(nums[i])

    return result

nums = [6,5,3,5,2,8,3]
print(remove_duplicates_from_front(nums))