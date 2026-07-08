class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

def print_card(self):
	print(f"{self.rank} of {self.suit}")
	
card = Card("Clubs", "Ace")
card.suit = "Hearts"
print_card(card)