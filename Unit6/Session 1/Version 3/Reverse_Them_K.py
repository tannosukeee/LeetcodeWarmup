class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_first_k(head, k):
    if head == None or k <= 1:
        return head
    
    prev = None
    curr = head
    count = 0

    tail = head

    while curr != None and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1
    tail.next = curr
    return prev

def print_list(head):
    curr = head

    while curr is not None:
        print(curr.value, end="")
        if curr.next is not None:
            print(" -> ", end="")
        curr = curr.next

    print()


# 1 -> 2 -> 3 -> 4 -> 5
node5 = Node(5)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
head = Node(1, node2)

new_head = reverse_first_k(head, 3)
print_list(new_head)