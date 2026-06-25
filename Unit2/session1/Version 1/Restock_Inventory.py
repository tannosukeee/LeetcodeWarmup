def restock_inventory(current_inventory, restock_list):
    for i in restock_list:
        if i not in current_inventory:
            current_inventory[i] = restock_list[i]
        else:
            current_inventory[i] += restock_list[i]
    
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))