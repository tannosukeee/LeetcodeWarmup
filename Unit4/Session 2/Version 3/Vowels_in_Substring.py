def max_vowels(s, k):
	vow = "ueoai"
	i = 0
	j = k
	count = 0
	max = 0
	while j <= len(s):
		for num in range(i, j):
			if s[num] in vow:
				count += 1
		if count > max:
			max = count
		i += 1
		j += 1
		count = 0
	return max

s = "abciiidef"
print(max_vowels(s, 3))

print(max_vowels(s, 5))