def string_to_integer_mapping(s):
    result = []
    for i in range(len(s)):
        result.append(int(s[i]))
    
    return result

s="12345"
print(string_to_integer_mapping(s))