def is_long_pressed(name, typed):
    i = 0
    j = 0
    while i < len(name):
        if name[i] == typed[j]:
            i += 1
            j += 1
        else:
            if typed[j] == name[i - 1]:
                j += 1
            else:
                return False
    
    return True

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))