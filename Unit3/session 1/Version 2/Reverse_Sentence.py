def reverse_sentence(sentence):
    result = sentence.split()
    left = 0
    right = len(result) - 1

    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    
    s = " ".join(result)
    return s

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))