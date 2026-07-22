class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        sum1 = 0
        for k in range(len(self.race_outcomes)):
            sum1 += self.race_outcomes[k]
        avg1 = sum1 / len(self.race_outcomes)
        sum = 0
        result = []
        result.append(avg1)
        for i in range(len(opponents)):
            if len(opponents[i].race_outcomes) != len(self.race_outcomes):
                return None
            else:
                for j in range(len(opponents[i].race_outcomes)):
                    sum += opponents[i].race_outcomes[j]
                result.append(sum / len(opponents[i].race_outcomes))
                sum = 0
        result.sort()
        return result.index(avg1) + 1
    
player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents)}")