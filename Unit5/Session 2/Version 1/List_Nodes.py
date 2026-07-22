class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	result = []
	curr = head
	for i in range(n):
		result.append(curr.value)
		if curr.next is None:
			break
		else:
			curr = curr.next
	return result

# linked list: a -> b -> c
c = Node("c")
b = Node("b", c)
a = Node("a", b)

head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
l = Node("l")
k = Node("k", l)
j = Node("j", k)
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)