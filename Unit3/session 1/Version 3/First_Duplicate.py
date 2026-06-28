def first_repeated_char(s):
    for i in range(len(s)):
        if s[i] in s[:i]:
            return i
    
    return None

s = "hello world"
s2 = "aAbBCC"
s3 = "abcdefg"

print(first_repeated_char(s))
print(first_repeated_char(s2))
print(first_repeated_char(s3))