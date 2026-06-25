def build_inventory(product_names, product_prices):
    result = {}

    if len(product_names) != len(product_prices):
        return result
    
    for i in range(len(product_prices)):
        result[product_names[i]] = product_prices[i]
    
    return result

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))