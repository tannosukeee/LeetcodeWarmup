class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_loop_start(head):
    if head == None or head.next == None:
        return None
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            start = head
            while start != slow:
                start = start.next
                slow = slow.next
            return start
    return None

