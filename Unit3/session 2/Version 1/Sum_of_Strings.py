def sum_of_number_strings(nums):
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)