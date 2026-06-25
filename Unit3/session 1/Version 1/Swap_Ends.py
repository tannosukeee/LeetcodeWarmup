def swap_ends(my_str):
    lst = list(my_str)
    lst[0], lst[len(lst) - 1] = lst[len(lst) - 1], lst[0]
    str = "".join(lst)
    return str

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)