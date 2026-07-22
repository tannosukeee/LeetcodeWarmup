class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def frequency_map(head):
	result = {}
	if head == None:
		return result
	curr = head
	while curr != None:
		if curr.value not in result:
			result[curr.value] = 1
		else:
			result[curr.value] += 1
		curr = curr.next
	return result
