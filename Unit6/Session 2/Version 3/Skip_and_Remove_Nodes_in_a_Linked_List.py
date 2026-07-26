class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
def skip_and_remove(head, m, n):
	if head == None:
		return None
	if n == 0:
		return head

	curr = head

	while curr != None:
		for _ in range(m - 1):
			if curr is None:
				return head
			curr = curr.next
		if curr is None:
			return head

		temp = curr.next
		for _ in range(n):
			if temp is None:
				break
			temp = temp.next

		curr.next = temp
		curr = temp

	return head