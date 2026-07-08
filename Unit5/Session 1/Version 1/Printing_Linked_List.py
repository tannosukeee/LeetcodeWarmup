class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	result = []
	curr = head
	while curr is not None:
		result.append(curr.value)
		curr = curr.next
	print(" -> ".join(result))

node_5 = Node("e")
node_4 = Node("d", node_5)
node_3 = Node("c", node_4)
node_2 = Node("b", node_3)
node_1 = Node("a", node_2)

print_linked_list(node_1)