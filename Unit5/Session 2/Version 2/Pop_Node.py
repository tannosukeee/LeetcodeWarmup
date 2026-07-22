class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_pop(head, i):
	count = 0
	curr = head
	if head == None:
		return None
	if i == 0:
		return curr.next
	while curr != None and count < i - 1:
		curr = curr.next
		count += 1
	
	if curr == None or curr.next == None:
		return None
	curr.next = curr.next.next
	return head

num3 = Node(30)
num2 = Node(20, num3)
num1 = Node(10, num2)

head = ll_pop(num1, 1)	