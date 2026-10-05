def is_nested(s):
    if s == "":
        return True
    elif s[0] == "(" and s[-1] == ")":
        return is_nested(s[1 : -1])
    else:
        return False

print(is_nested("(()"))
