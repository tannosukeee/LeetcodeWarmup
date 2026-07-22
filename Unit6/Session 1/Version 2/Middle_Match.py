class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def middle_match(head, val):
    if head == None or head.next == None:
        return head
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    if slow.value == val:
        return True
    else:
        return False

head = Node("1", Node("2", Node("3")))
val = "2"
print(middle_match(head, val))

head = Node("1", Node("2", Node("3", Node("4"))))
val = "2"
print(middle_match(head, val))