def find_difference(s1, s2):
    for letter in s2:
        if letter not in s1:
            return letter
        
s1 = "abcd"
s2 = "baedc"
print(find_difference(s1, s2))