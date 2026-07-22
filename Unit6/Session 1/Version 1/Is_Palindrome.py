class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
     if head == None or head.next == None:
         return False
     slow = head
     fast = head

     while fast is not None and fast.next != None:
         slow = slow.next
         fast = fast.next.next
     prev = None
     curr = slow

     while curr != None:
         next_node = curr.next
         curr.next = prev
         prev = curr
         curr = next_node
     left = head
     right = prev
     while right != None:
         if left.value != right.value:
             return False
         left = left.next
         right = right.next
     return True