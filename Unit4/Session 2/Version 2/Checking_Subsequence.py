def is_subsequence(s, t):
	i = 0
	j = 0
	while i < len(s) and j < len(t):
		if s[i] == t[j]:
			i += 1
			j += 1
		else:
			j += 1
	if i < len(s) - 1:
		return False
	else:
		return True

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))