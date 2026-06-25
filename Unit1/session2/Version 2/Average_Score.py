def average(scores):
    sum = 0
    for num in scores:
        sum += num
    
    return sum / len(scores)

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)