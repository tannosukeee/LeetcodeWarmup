def quality_control(product_scores, threshold):
    for key in product_scores:
        if product_scores[key] >= threshold:
            product_scores[key] = "pass"
        elif product_scores[key] < threshold:
            product_scores[key] = "fail"
    
    return product_scores

product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))