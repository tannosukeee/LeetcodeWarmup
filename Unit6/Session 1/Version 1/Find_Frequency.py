class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	count = 0
	curr = head
	while curr != None:
		if curr.value == val:
			count += 1
			curr = curr.next
		else:
			curr = curr.next
	return count