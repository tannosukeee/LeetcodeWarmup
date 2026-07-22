class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def delete_tail(head):
	curr = head
	if curr == None or curr.next == None:
		return None
	while curr != None:
		if curr.next.next == None:
			curr.next = None
			curr = curr.next
		else:
			curr = curr.next
	return None

def print_linked_list(head):
    curr = head
    values = []

    while curr is not None:
        values.append(str(curr.value))
        curr = curr.next

    print(" -> ".join(values))


num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

delete_tail(num1)
print_linked_list(num1)