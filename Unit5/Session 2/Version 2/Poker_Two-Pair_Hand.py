class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

def is_two_pair(player_hand):
	result = {}
	for i in range(len(player_hand)):
		if player_hand[i].rank not in result:
			result[player_hand[i].rank] = 1
		else:
			result[player_hand[i].rank] += 1
	count = 0
	for key in result:
		if result[key] >= 2:
			count += 1
	if count >= 2:
		return True
	else:
		return False

card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))