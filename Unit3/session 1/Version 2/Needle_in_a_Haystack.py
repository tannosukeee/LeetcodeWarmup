def find_the_needle(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] in needle and haystack[i : i + len(needle)] == needle:
            return i
        
    return -1

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))