def remove_char(s, n):
    lst = list(s)
    for i in range(len(lst)):
        if i == n:
            lst.pop(i)
    
    s = "".join(lst)
    return s

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)