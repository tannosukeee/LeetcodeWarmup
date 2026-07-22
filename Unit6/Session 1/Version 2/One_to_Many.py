class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node("Mario", Node("Luigi", Node("Wario")))
node_3 = Node("Wario")
node_2 = Node("Luigi", node_3)
node_1 = Node("Mario", node_2)