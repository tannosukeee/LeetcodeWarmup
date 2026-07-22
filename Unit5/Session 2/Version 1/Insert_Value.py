class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
	new_node = Node(val)
	curr = head
	count = 0
	if head is None:
		return new_node

	if i == 0:
		new_node.next = curr
		return new_node

	while curr.next is not None and count < i - 1:
		curr = curr.next
		count += 1
		
	new_node.next = curr.next
	curr.next = new_node

	return head