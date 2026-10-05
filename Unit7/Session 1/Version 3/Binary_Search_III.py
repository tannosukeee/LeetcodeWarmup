def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list

	# While left pointer is less than right pointer:
		# Find the middle index of the array

		# If the middle value is the target value, return True
		# If the middle value is smaller than the target value, search the right half of the list
		# If the middle value is greater than the target value, search the left half of the list

	# Return False if the target element has not been found
    l = 0
    r = len(lst) - 1

    while l < r:
        m = (l + r) // 2

        if lst[m] == target:
            return True
        elif lst[m] < target:
            l = m + 1
        else:
            r = m - 1
    return False

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

print(binary_search(lst, target))
