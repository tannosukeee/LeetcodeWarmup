def is_power_of_four(n):
    if n == 1:
        return True
    if n < 1 or n % 4 != 0:
        return False
    return is_power_of_four(n // 4)

print(is_power_of_four(16))
print(is_power_of_four(8))