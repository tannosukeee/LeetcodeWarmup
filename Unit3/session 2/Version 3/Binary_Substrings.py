def binary_substrings_count(s):
    result = []

    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(count)
            count = 1
    
    result.append(count)
    total = 0
    for i in range(1, len(result)):
        total += min(result[i - 1], result[i])
    
    return total

s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))