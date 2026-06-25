def concatenate_list(nums):
    n = len(nums)
    ans = []
    for i in range(n):
        ans.append(nums[i])
    
    for i in range(n):
        ans.append(nums[i])
    
    return ans

print(concatenate_list([1,2,3,4]))

'''
def concatenate_list(nums):
    return nums * 2
'''