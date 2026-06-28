def find_poisoned_duration(time_series, duration):
    total = 0
    for i in range(len(time_series) - 1):
        gap = time_series[i + 1] - time_series[i] - 1

        if gap < duration:
            total += gap
        else:
            total += duration
    
    total += duration
    return total

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)