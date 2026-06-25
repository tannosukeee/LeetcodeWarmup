def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return round(bill * 10 / 100, 4)
    elif service_quality == "average":
        return round(bill * 15 / 100, 4)
    elif service_quality == "excellent":
        return round(bill * 20 / 100, 4)
    else:
        return None

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)