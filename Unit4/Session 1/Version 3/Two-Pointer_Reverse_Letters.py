def reverse_only_letters(s):
    lst = list(s)
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left].isalpha():
            if lst[right].isalpha():
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            if lst[right].isalpha():
                left += 1
            else:
                left += 1
                right -= 1
    
    return "".join(lst)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)