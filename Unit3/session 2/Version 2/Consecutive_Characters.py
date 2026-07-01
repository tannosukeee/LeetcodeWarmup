def count_consecutive_characters(str1):
    max = 1
    count = 1
    for i in range(1, len(str1)):
        if str1[i] == str1[i - 1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    
    if count > max:
        max = count
    return max

str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)
str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)