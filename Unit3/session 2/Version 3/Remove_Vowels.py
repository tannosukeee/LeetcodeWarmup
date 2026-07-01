def remove_vowels(s):
    vow = "ueoai"
    result = list(s)
    for letter in result:
        if letter in vow:
            result.remove(letter)
    st = "".join(result)    
    return st

s = "Hello World"
new_string = remove_vowels(s)
print(new_string)