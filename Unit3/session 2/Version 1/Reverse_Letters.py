def reverse_only_letters(s):
    lst = list(s)
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left].isalpha() == False:
            left += 1
        elif lst[right].isalpha() == False:
            right -= 1
        else:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
    s = "".join(lst)
    return s

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)