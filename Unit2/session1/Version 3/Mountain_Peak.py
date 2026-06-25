def peak_index_in_mountain_list(lst):
    max = 0
    index = 0

    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
            index = i
    
    return index

mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)