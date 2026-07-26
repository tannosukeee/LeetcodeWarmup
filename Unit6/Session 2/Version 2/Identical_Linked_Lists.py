class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_identical(head_a, head_b):
    curr1 = head_a
    curr2 = head_b

    while curr1 != None and curr2 != None:
        if curr1.value != curr2.value:
            return False
        else:
            curr1 = curr1.next
            curr2 = curr2.next
    return curr1 == None and curr2 == None