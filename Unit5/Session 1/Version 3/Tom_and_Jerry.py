class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

mouse = Node("Jerry")
cat = Node("Tom", mouse)

# Problem 10: add dog so the list is dog -> cat -> mouse
dog = Node("Spike", cat)

print(dog.value)
print(dog.next.value)
print(dog.next.next.value)
print(cat.value)
print(cat.next.value)
print(mouse.next)