# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
  result = [] # List to store the merged result
  i = j = 0 # Pointers to iterate over left and right input arrays

	# Compare elements from left and right halves of the list and add them to the
	# result list in the correct order
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
  # Add any remaining elements from the left half to the result list
  while i < len(left):
      result.append(left[i])
      i += 1

  # Add any remaining elements from the right half to the result list
  while j < len(right):
      result.append(right[j])
      j += 1

  return result

def merge_sort(lst):
    if len(lst) == 0:
       return []
    if len(lst) == 1:
       return lst
    else:
       mid = (0 + len(lst))// 2
       return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))

print(merge_sort([5, 3, 4, 2, 1]))
