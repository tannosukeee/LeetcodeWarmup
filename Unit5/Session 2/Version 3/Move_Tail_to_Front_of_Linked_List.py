class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def tail_to_head(head):
    if head == None:
        return None
    if head.next == None:
        return head
    curr = head
    new_curr = head.next
    while new_curr != None:
        if new_curr.next == None:
            curr.next = None
            new_curr.next = head
            return new_curr
        else:
            curr = curr.next
            new_curr = new_curr.next
