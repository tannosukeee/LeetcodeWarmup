def min_distance(words, word1, word2):
    if word1 not in words or word2 not in words:
        return None
    w1 = []
    w2 = []
    for i in range(len(words)):
        if words[i] == word1:
            w1.append(i)
        elif words[i] == word2:
            w2.append(i)
    
    if w1[0] > w2[0]:
        min = w1[0] - w2[0]
    elif w2[0] > w1[0]:
        min = w2[0] - w1[0]

    for num1 in w1:
        for num2 in w2:
            if num1 > num2 and num1 - num2 < min:
                min = num1 - num2
            elif num2 > num1 and num2 - num1 < min:
                min = num2 - num1
    
    return min

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)