class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_last_node_in_cycle(head):
    if head == None:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            start = head
            while start != slow:
                start = start.next
                slow = slow.next
            curr = start
            while curr.next != start:
                curr = curr.next
            return curr
    return None

num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num4 = Node("num4")

num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2

last = find_last_node_in_cycle(num1)
print(last.value)