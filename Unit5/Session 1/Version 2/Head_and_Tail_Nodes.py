class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node(100)
tail = Node(200)
head.next = tail

print(head.value) 
print(head.next.value) 
print(tail.value) 
print(tail.next) 