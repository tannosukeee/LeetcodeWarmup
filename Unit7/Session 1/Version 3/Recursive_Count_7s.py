def count_sevens(n):
    s = str(n)
    count = 0
    for i in range(len(s)):
        if s[i] == "7":
            count += 1
    return count

print(count_sevens(727))
