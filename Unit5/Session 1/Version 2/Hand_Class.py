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

class Hand:
    def __init__(self):
        self.cards = []
     
    def add_card(self, card):
        self.cards.append(card)
    def remove_card(self, card):
        self.cards.remove(card)

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]

for card in player1_hand.cards:
    print(card.suit, card.rank)