class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def increment_ll(head):
    if head == None:
        return None
    curr = head
    while curr != None:
        curr.value += 1
        curr = curr.next
    return head
    