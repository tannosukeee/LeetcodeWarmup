def calculate_gpa(report_card):
    sum = 0

    for i in report_card:
        if report_card[i] == "A":
            sum += 4
        elif report_card[i] == "B":
            sum += 3
        elif report_card[i] == "C":
            sum += 2
        elif report_card[i] == "D":
            sum += 1
    
    return sum / len(report_card)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))