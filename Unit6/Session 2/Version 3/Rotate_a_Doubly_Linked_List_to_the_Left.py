class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


def rotate_doubly_linked_list(head, k):
    if not head or k == 0:
        return head
    
    last = head
    length = 1
    while last.next:
        last = last.next
        length += 1
    
    k = k % length
    if k == 0:
        return head
    
    new_tail = head
    for _ in range(k - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    
    last.next = head
    head.prev = last
    new_tail.next = None
    new_head.prev = None
    
    return new_head