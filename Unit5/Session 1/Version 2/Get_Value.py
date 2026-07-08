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
	def get_value(self):
		int_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
		if self.rank in int_rank:
			return self.rank
		elif self.rank == "Ace":
			return 1
		elif self.rank == "Jack":
			return 11
		elif self.rank == "Queen":
			return 12
		elif self.rank == "King":
			return 13
		else:
			return None

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())