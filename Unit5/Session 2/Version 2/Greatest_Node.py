class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def find_max(head):
	if head == None:
		return 0
	elif head.next == None:
		return head.value
	max_val = head.value
	curr = head
	while curr is not None:
		if curr.value > max_val:
			max_val = curr.value
			curr = curr.next
		else:
			curr = curr.next
	return max_val

num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)

max_val = find_max(num1)
print(max_val)