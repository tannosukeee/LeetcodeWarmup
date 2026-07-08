class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def is_valid(self):
		valid_suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
		valid_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		if self.suit in valid_suit and self.rank in valid_rank:
			return True
		else:
			return False

def print_card(self):
	print(f"{self.rank} of {self.suit}")
	
my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())