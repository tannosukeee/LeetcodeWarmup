class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def copy_ll(head):
    if head == None:
        return head
    new_head = Node(head.value)
    old = head.next
    new = new_head

    while old != None:
        new_node = Node(old.value)
        new.next = new_node

        old = old.next
        new = new.next
    return new_head
node3 = Node(7)
node2 = Node(6, node3)
head = Node(5, node2)

copy = copy_ll(head)

print(head.value, copy.value)

head.value = 10

print(head.value, copy.value)