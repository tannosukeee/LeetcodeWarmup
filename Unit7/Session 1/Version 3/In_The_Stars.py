def insert_stars(s):
    # If the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    # Otherwise, insert '*' between the first character and the rest, then recurse
    else:
        return s[0] + "*" + insert_stars(s[1:])


print(insert_stars("abc"))

def insert_stars_iterative(s):
    for i in range(len(s) - 1):
        print(s[i] + "*", end="")
    print(s[len(s) - 1])
    
insert_stars_iterative("abc")
