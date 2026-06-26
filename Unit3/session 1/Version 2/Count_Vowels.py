def vowel_count(s):
    vowels = "ueoai"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    
    return count

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)