class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

mouse = Node("Jerry")
cat = Node("Tom", mouse)
cheese = Node("Gouda")
mouse.next = cheese
        
print(cat.next is mouse)      
print(cat.next.value)         
print(mouse.next) 