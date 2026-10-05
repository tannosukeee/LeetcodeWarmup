def count_substring(s, sub):
    if s == "" or sub == "":
        return 0
    for i in range(len(sub)):
        if s[i] != sub[i]:
            return count_substring(s[1:], sub)
    return 1 + count_substring(s[len(sub) :], sub)

s = "abcdeabcde"
sub = "abc"
print(count_substring(s, sub))
