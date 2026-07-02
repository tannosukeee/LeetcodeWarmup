def find_content_children(g, s):
    i = 0
    j = 0
    count = 0
    g.sort()
    s.sort()
    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            count += 1
            i += 1
            j += 1
        else:
            i += 1
    
    print(count)

g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

find_content_children(g, s) 
# Output: 2 

g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

find_content_children(g, s) 
# Output: 2 