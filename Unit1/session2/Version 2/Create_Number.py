def list_to_number(digits):
    number = 0

    for digit in digits:
        number = number * 10 + digit

    return number

digits = [1, 0, 3]
number = list_to_number(digits)
print(number)