class Player():
	def  __init__(self, character, kart, opponent=None):
		self.character = character
		self.kart = kart
		self.items = []
		self.ahead = opponent
		
def get_place(my_player):
	curr = my_player
	rank = 1
	while curr.ahead is not None:
		rank += 1
		curr = curr.ahead
	return rank

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
print(player1_rank)

player2_rank = get_place(peach)
print(player2_rank)

player3_rank = get_place(mario)
print(player3_rank)