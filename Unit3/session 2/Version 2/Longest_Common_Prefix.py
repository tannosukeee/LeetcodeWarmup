def longest_common_prefix(strings):
    for i in range(len(strings)):
        char = strings[0][i]

        for word in strings[1:]:
            if i >= len(word) or word[i] != char:
                return strings[0][:i]
    return strings[0]

strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)