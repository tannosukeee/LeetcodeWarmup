class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def detect_and_remove_cycle(head):
    if head is None:
        return None
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            start = head
            while start != slow:
                start = start.next
                slow = slow.next
            tail = start.next
            while tail.next != start:
                tail = tail.next
            tail.next = None
    return head