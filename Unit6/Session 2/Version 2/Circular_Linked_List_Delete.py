class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_node(head, val):
    if head is None:
        return None
    if head.value == val and head.next == head:
        return None
    if head.value == val:
        curr = head
        while curr.next != head:
            curr = curr.next
        curr.next = head.next
        head = head.next
        return head
    else:
        prev = head
        curr = head.next
        while curr != head:
            if curr.value == val:
                prev.next = curr.next
                return head
            else:
                prev = prev.next
                curr = curr.next
        return head
    