class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(head):
    if head == None or head.next == None:
        return 0
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            curr = slow.next
            while curr != slow:
                count += 1
                curr = curr.next
            return count
    return 0
