def squares(nums):
    result = []
    for num in nums:
        num = num * num
        result.append(num)
    
    return result

print(squares([1,2,3,4]))