def count_good_substrings(s):
    left = 0
    right = 3
    count = 0

    while right <= len(s):
        if s[left] in s[left + 1 : right] or s[left + 1] in s[left + 2 : right]:
            left += 1
            right += 1
        else:
            count += 1
            left += 1
            right += 1
    
    return count

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))