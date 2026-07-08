class Card():
	def  __init__(self, suit, rank, next = None):
		self.suit = suit
		self.rank = rank
		self.next = next
		
def print_hand(starting_card):
	result = []
	curr = starting_card
	while curr is not None:
		result.append(curr)
		curr = curr.next
	return result

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print(print_hand(card_one))