def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("Nice hand!")
    else:
        print("Hit me!")

blackjack(21)
blackjack(24)
blackjack(19)
blackjack(10)