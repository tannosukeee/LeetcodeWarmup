class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def find_middle_node(head):
	if head == None:
		return None
	curr = head
	count = 0
	while curr != None:
		count += 1
		curr = curr.next
	mid = (count - 1) // 2
	count = 0
	curr2 = head
	while count < mid:
		curr2 = curr2.next
		count += 1
	return curr2


	