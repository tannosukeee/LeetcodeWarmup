class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

card = Card("Spades", "8")
print(card.suit)
print(card.rank)