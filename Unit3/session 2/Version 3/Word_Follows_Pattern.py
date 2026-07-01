def wordPattern(pattern, s):
    strings = list(s.split(" "))
    pat = list(pattern)

    if len(strings) != len(pat):
        return False
    
    result = {}
    for i in range(len(strings)):
        if pat[i] not in result:
            result[pat[i]] = strings[i]
        else:
            if result[pat[i]] != strings[i]:
                return False
    
    return True

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))