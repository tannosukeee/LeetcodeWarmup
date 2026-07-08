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
		
def sum_hand(hand):
	sum = 0
	for card in hand.cards:
		if card.rank == None:
			return None
		else:
			sum += int(card.get_value())
	return sum

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)