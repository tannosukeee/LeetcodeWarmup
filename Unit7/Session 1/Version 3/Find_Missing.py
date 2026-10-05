def find_missing(nums):
    count = 0
    for n in nums:
        if n != count:
            return count
        else:
            count += 1

nums = [0, 1, 3]
print(find_missing(nums))
