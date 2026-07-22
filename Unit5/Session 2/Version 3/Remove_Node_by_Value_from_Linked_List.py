class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def ll_remove(head, val):
    if head == None:
        return None
    if head.value == val:
        if head.next == None:
            return None
        else:
            curr = head.next
            head.next = None
            return curr
    curr = head
    new_curr = head.next
    while new_curr != None:
        if new_curr.value == val:
            curr.next = new_curr.next
            break
        else:
            curr = curr.next
            new_curr = new_curr.next
    return head

