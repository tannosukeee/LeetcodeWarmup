def reverse_prefix(word, ch):
    left = 0
    right = 0
    for letter in word:
        if letter == ch:
            right = word.find(letter)
            break
    
    lst = list(word)
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return "".join(lst)

word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)