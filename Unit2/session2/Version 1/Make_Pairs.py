def divide_list(nums):
    result = {}
    for num in nums:
        if num not in result:
            result[num] = 1
        else:
            result[num] += 1
    for key in result:
        if result[key] % 2 != 0:
            return False
    
    return True

nums = [3,2,3,2,2,2]
print(divide_list(nums))

nums = [1,2,3,4]
print(divide_list(nums))