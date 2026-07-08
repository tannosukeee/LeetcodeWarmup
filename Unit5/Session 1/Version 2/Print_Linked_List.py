class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	curr = head
	result = []
	while curr is not None:
		result.append(curr.value)
		curr = curr.next
	print(result)

e = Node("e")
d = Node("d", e)
c = Node("c", d)
b = Node("b", c)
a = Node("a", b)

print_linked_list(a)