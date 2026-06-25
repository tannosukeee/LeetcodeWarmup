def get_odds(nums):
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)