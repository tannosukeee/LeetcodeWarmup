def update_or_warn(records, item, update_value):
    if item not in records:
        print(item + " not found!")
    else:
        records[item] = update_value
    return records

records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "grape", 4)
# Print the input dictionary after running the function to check if it was modified
print(records) 
update_or_warn(records, "banana", 5)
print(records)