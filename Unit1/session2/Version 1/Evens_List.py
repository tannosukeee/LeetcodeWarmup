def get_evens(lst):
    result = []

    for num in lst:
        if num % 2 == 0:
            result.append(num)

    return result

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)