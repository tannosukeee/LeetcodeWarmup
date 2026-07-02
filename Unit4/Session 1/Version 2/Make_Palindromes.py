def make_palindrome(s):
    lst = list(s)
    left = 0
    right = len(lst) - 1
    alph = "abcdefghijklmnopqrstuvwxyz"

    while left < right:
        if lst[left] != lst[right]:
            if alph.find(lst[left]) < alph.find(lst[right]):
                lst[right] = lst[left]
            else:
                lst[left] = lst[right]
        left += 1
        right -= 1
    result = "".join(lst)
    return result

s = "egcfe"
print(make_palindrome(s))

s = "abcd"
print(make_palindrome(s))

s = "seven"
print(make_palindrome(s))