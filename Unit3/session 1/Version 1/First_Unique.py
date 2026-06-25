def first_unique_char(my_str):
    for i in range(len(my_str)):
        if my_str[i] not in my_str[i + 1:] and my_str[i] not in my_str[:i]:
            return i
    
    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))