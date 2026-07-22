class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_element(head):
    if head == None:
        return None
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow
