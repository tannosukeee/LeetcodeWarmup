def ternary_search(lst, target):
    # Divide the array into three parts using two mid points (mid1 and mid2).
    left = 0
    right = len(lst) - 1
    # While the lower bound is less than or equal to the upper bound:
    while left <= right:
        offset = (right - left) // 3
        mid1 = left + offset
        mid2 = right - offset
	    # Compare the target value with the values at mid1 and mid2:
	        # If the target value matches mid1 or mid2
		        # the search is successful.
        if lst[mid1] == target:
            return mid1
        elif lst[mid2] == target:
            return mid2
	      # If the target is less than the value at mid1
		      # search between the lower bound and mid1 - 1.
        elif target < lst[mid1]:
            right = mid1 - 1
	      # If the target is between mid1 and mid2
		      # search between mid1 + 1 and mid2 - 1.
        elif target > lst[mid1] and target < lst[mid2]:
            left = mid1 + 1
            right = mid2 + 2
	      # If the target is greater than the value at mid2
		      # search between mid2 + 1 and the upper bound.
        elif target > lst[mid2]:
            left = mid2 + 1
  # Return -1, indicating the target is not in the array.
    return -1

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

print(ternary_search(lst, target))