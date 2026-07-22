class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

poliwag = Node("Poliwag")
poliwhirl = Node("Poliwhirl")
poliwrath = Node("Poliwrath")
poliwag.next = poliwhirl
poliwhirl.prev = poliwag
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl

print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)