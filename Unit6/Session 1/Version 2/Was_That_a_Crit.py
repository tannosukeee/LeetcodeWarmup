class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_critical_points(head):
    if head == None or head.next == None or head.next.next == None:
        return 0
    prev = head
    curr = head.next
    nxt = curr.next
    count = 0

    while nxt != None:
        if curr.value < prev.value and curr.value < nxt.value:
            count += 1
        elif curr.value > prev.value and curr.value > nxt.value:
            count += 1
        prev = prev.next
        curr = curr.next
        nxt = nxt.next
    return count

node8 = Node(3)
node7 = Node(1, node8)
node6 = Node(5, node7)
node5 = Node(3, node6)
node4 = Node(3, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
head = Node(1, node2)

print(count_critical_points(head))