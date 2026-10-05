def sqrt(x):
    num = 0
    while num < x:
        if num * num > x:
            return num - 1
        else:
            num += 1

print(sqrt(8))
