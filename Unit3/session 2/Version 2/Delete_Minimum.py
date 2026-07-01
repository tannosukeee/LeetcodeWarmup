def delete_minimum_elements(nums):
    return sorted(nums)
            
nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)