class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def ll_length(head):
	curr = head
	count = 0
	while curr != None:
		count += 1
		curr = curr.next
	return count

# Linked List: num1 -> num2 -> num3
num3 = Node('3')
num2 = Node('2', num3)
num1 = Node('1', num2)
head = num1
print(ll_length(head))

# Empty Linked List
head = None
print(ll_length(head))