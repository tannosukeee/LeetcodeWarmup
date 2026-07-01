def partition_label(s):
    last = {}
    for i, char in enumerate(s):
        last[char] = i
    
    result = []
    end = 0
    start = 0

    for i, char in enumerate(s):
        if last[char] > end:
            end = last[char]
        
        if i == end:
            size = i - start + 1
            result.append(size)
            start = i + 1
    
    return result

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))