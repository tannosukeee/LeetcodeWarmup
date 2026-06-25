def remove_items_below_price(items, price_threshold):
    result = []
    for key in list(items.keys()):
        if items[key] < price_threshold:
            items.pop(key)
            result.append(key)

    if len(result) == 0:
        return None
    else:
        return result

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)