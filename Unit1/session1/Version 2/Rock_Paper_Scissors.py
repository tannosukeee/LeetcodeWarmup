def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("It's a tie!")
        return
    
    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins!")
        elif player2 == "paper":
            print("Player 2 wins!")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins!")
        elif player2 == "rock":
            print("Player 2 wins!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins!")
        elif player2 == "scissors":
            print("Player 2 wins!")

rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")