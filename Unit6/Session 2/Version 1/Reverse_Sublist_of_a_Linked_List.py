class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse_between(head, m, n):
    if head == None or m >= n:
        return None

    dummy = Node(0, head)
    before_reverse = dummy

    for _ in range(m - 1):
        before_reverse = before_reverse.next

    prev = None
    curr = before_reverse.next
    reverse_tail = curr

    for _ in range(n - m + 1):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    before_reverse.next = prev
    reverse_tail.next = curr

    return dummy.next

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

new_head = reverse_between(head, 2, 5)
print_list(new_head)