def get_items_to_restock(products, restock_threshold):
    result = []

    for key in products:
        if products[key] < restock_threshold:
            result.append(key)
    
    return result

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold))