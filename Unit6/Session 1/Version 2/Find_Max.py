class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def find_max(head):
	if head == None:
		return Node
	if head.next == None:
		return head.value
	max_value = head.value
	curr = head.next
	while curr != None:
		if curr.value > max_value:
			max_value = curr.value
			curr = curr.next
		else:
			curr = curr.next
	return max_value
head = Node("5", Node("6", Node("7", Node("8"))))
print(find_max(head))