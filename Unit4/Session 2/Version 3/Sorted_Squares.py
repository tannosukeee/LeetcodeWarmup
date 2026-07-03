def sorted_squares(nums):
    result = []
    for num in nums:
        result.append(num * num)
    
    result.sort()

    return result

nums = [1,2,3,4]
sq_nums = sorted_squares(nums)
print(sq_nums)
nums2 = [-4,-1,0,3,10]
sq_nums2 = sorted_squares(nums2)
print(sq_nums2)