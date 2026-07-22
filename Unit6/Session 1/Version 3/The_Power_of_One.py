class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# Recreate this list in a single line of code
head = Node("Ash")
misty = Node("Misty")
brock = Node("Brock")
head.next = misty
misty.next = brock

head = Node("Ash", Node("Misty", Node("Brock")))