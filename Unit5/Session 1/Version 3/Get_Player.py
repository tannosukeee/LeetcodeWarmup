class Player():
	def  __init__(self, character, kart):
		self.character = character
		self.kart = kart
	def get_player(self):
		return f"{self.character} driving the {self.kart}"

player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Pirahna Prowler")
print("Match: " + player_one.get_player() + " vs " + player_two.get_player())