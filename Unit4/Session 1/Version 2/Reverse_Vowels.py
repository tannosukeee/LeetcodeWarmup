def reverse_vowels(s):
    lst = list(s)
    left = 0
    right = len(lst) - 1
    vow = "ueoai"

    while left < right:
        if lst[left] in vow and lst[right] in vow:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        elif lst[left] not in vow and lst[right] in vow:
            left += 1
        elif lst[left] in vow and lst[right] not in vow:
            right -= 1
        else:
            left += 1
            right -= 1
    return "".join(lst)

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)
