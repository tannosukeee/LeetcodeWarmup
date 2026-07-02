def find_highest_exponent(base, limit):
    for i in range(limit):
        if base ** i > limit:
            return i - 1

exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)