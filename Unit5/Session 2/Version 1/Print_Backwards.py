class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def print_reverse(tail):
	curr = tail
	while curr != None:
		print(curr.value, end=" ")
		curr = curr.prev
		
poliwag = Node("Poliwag")
poliwhirl = Node("Poliwhirl")
poliwrath = Node("Poliwrath")
poliwag.next = poliwhirl
poliwhirl.prev = poliwag
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
print_reverse(poliwrath)