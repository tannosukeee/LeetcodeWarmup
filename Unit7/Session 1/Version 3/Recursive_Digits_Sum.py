def sum_digits(n):
    if n == "":
        return 0
    else:
        return int(str(n)[0]) + sum_digits(str(n)[1:])

print(sum_digits(523))
