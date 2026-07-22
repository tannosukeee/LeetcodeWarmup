class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    if head == None or head.next == None:
        return False
    
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
            return start == head
    return False