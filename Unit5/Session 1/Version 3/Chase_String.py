class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
def chase_list(head):
	curr = head
	while curr is not None:
		if curr.next is None:
			print(curr.value)
			break
		else:
			print(curr.value + " chases", end=" ")
			curr = curr.next

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))