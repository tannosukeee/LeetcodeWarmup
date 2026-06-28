def length_of_longest_substring(s):
	longest = 0
	for i in range(len(s)):
		lst = []
		for j in range(i, len(s)):
			if s[j] not in lst:
				lst.append(s[j])
			else:
				break
		longest = max(longest, len(lst))
	return longest

s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)