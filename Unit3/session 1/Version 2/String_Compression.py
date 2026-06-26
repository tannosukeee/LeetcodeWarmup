def compress_string(my_str):
    count = 1
    lst = list(my_str)
    l = []
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            l.append(lst[i - 1])
            l.append(str(count))
            count = 1
    l.append(lst[-1])
    l.append(str(count))

    s = "".join(l)
    if len(s) > len(my_str):
        return my_str
    else:
        return s

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)