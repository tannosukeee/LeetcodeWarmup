class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, val):
	new_node = Node(val, head)
	return new_node