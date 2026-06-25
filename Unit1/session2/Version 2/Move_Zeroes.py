def move_zeroes(nums):
    result = []
    count = 0

    for num in nums:
        if num != 0:
            result.append(num)
        else:
            count += 1
    
    for i in range(count):
        result.append(0)
    
    return result

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)