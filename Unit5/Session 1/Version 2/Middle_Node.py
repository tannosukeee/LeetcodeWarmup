class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node(100)
tail = Node(200)
middle = Node(150)
head.next = middle
middle.next = tail

print(head.next.value) 
print(middle.next.value)
print(tail.next) 