def update_score(scores, players, points):
    if players not in scores:
        scores[players] = points
    else:
        scores[players] += points

    return scores

scores = {"Alice": 100, "Bob": 90}
update_score(scores, "Alice", 10)
print(scores)
update_score(scores, "Calvin", 20)
print(scores)
update_score(scores, "Calvin", 5)
print(scores)