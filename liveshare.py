'''
1. Understand:
- Create a 1 object Card and assign it into variable named card

2. Match:
card = Card(arg1, arg2)

3. Plan:
- Use a class name Card
- Pass "Spades" as the first argument
- Pass "8" as the second argument
- Store the new object into card

4. Implement
'''

class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

card = Card("Spares", "8")

'''
5. Review
'''
print(card.suit)
print(card.rank)

'''
6. Evaluate:
- Time complexity: O(1)
- Space complexity: O(1)
'''

'''
Problem 2

1. Understand:
-edit card class with a method called print_card

2. Match:
print_card(self)

3. Plan:
-define function print_card with self as parameter
-store clubs for suit 
-store ace for rank
-call the print method 

4. Implement
'''
def print_card(self):
	print(f"{self.rank} of {self.suit}")

card = Card("Clubs", "Ace")	
print_card(card)

'''
5.Review 
'''


#Evaluate:
#time complexity 0(1)
#space complexity 0(1)

'''
1. Understand:
- Change the suit of card to "Hearts"

2. Match:
- card.suit = arg

3. Plan:
- Change suit of card by calling card.suit equal to Hearts

4. Implement:
'''
card.suit = "Hearts"

'''
5. Review
'''
print_card(card)

'''
6. Evaluate
- Time complexity: O(1)
- Space complexity: O(1)
'''

''''
1. Understand:
-make new method is_valid return true if suit is one of the values and rank is one of the values 

2. Match 
is_valid(self)

2. Plan:
-define function is_valid with self as parameter
-return true if suit is in the following values: "Hearts, "Spades", "Clubs", "Diamonds"
-return true if rank has the following values 
-retirm false of dpesnt meet the above conditions

'''

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	
	def is_valid(self):
		valid_suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
		valid_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		
		if self.suit in valid_suits and self.rank in valid_rank:
			return True
		else:
			return False

'''
5. Review
'''

my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())

'''
1. Understand:
- The function get_value() receive the rank of card as a input and return a integer based off the rank

2. Match:
card.get_value()

3. Plan:
- Define the function get_value()
- Make a list of integer has all the rank number in card (have to be integers)
- Check if card.rank in the list of integer or not, if yes, return card.rank
- Check if card.rank is "Ace", if yes, return 1
- Check if card.rank is "Jack", if yes, return 11
- Check if card.rank is "Queen", if yes, return 12
- Check if card.rank is "King", if yes, return 13
- Else, return None

4. Implement:
'''

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	
	def is_valid(self):
		valid_suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
		valid_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		
		if self.suit in valid_suits and self.rank in valid_rank:
			return True
		else:
			return False
	def get_value(self):
		rank_int = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
		if self.rank in rank_int:
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

'''
5. Review
'''
card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())

'''
6. Evaluate:
- Time complexity: O(1)
- Space complexity: O(1)
'''

'''
1. Understand:
-create a new class called hand and implement add card and remove card method

2. Match:
class Hand():
	add_card(self, card)'
	''

#thank you