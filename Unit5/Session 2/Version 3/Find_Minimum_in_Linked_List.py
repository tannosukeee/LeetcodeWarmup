class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_min(head):
    if head == None:
        return None
    if head.next == None:
        return head.value
    min_val = head.value
    curr = head.next
    while curr != None:
        if curr.value < min_val:
            min_val = curr.value
            curr = curr.next
        else:
            curr = curr.next
    return min_val
