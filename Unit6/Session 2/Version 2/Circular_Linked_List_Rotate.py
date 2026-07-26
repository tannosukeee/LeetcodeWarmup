class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def rotate_right(head, k):
    len = 1
    tail = head
    while tail.next != None:
        len += 1
        tail = tail.next

    k = k % len
    if k == 0:
        return head
    
    tail.next = head
    new_tail = head
    for _ in range(len - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head