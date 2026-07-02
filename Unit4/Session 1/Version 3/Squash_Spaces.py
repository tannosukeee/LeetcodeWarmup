def squash_spaces(s):
    result = []

    for i in range(len(s)):
        if s[i] != " ":
            result.append(s[i])
        else:
            if result and result[-1] != " ":
                result.append(s[i])
    
    if result[-1] == " ":
        result.pop(-1)
    
    return "".join(result)

print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))