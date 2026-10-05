def merge_sort(arr):
    # If the length of the list is 0-1, the list is already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle index of the array
    mid = len(arr) // 2
    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to merge_sort for sorting the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted arrays
    return merge(left_half, right_half)


def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1
    if i == len(left) - 1:
        for l in range(i, len(left)):
            result.append(left[l])
        return result
    else:
        for k in range(j, len(right)):
            result.append(right[k])
        return result

print(merge([1, 3, 5], [2, 4]))
print(merge([1, 2], []))
print(merge([1, 2, 3], [4, 5]))
