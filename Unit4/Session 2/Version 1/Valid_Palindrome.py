def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    ss = ""
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            ss = s[: left] + s[left + 1:]
            break
    
    if ss != "" and ss != ss[::-1]:
        return False
    else:
        return True
    
s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))