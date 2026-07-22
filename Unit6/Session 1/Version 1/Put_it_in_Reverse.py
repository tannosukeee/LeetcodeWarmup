class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    if head == None or head.next == None:
        return head
    prev = None
    curr = head
    while curr != None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev