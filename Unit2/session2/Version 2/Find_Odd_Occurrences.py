def find_odd_occurrences(numbers):
    result = []
    for num in numbers:
        if num not in result:
            if num % 2 != 0:
                result.append(num)
    
    return result

numbers = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)