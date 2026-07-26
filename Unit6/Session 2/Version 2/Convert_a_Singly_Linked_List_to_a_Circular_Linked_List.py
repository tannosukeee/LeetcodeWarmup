class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def make_circular(head):
    if head == None:
        return head

    curr = head

    while curr:
        if curr.next == None:
            curr.next = head
            break
        curr = curr.next
    return head
