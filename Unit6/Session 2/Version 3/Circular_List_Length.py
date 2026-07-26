class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def circular_list_length(head):
    if head == None:
        return 0
    len = 1
    curr = head.next
    while curr != head:
        len += 1
        curr = curr.next

    return len