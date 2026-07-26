class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_cycle_nodes(head):
    result = []
    if head == None:
        return result
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
            result.append(start)
            start = start.next
            while start != slow:
                result.append(start)
                start = start.next
            return result
        
    return result
