class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_two_lists(head_a, head_b):
    if head_a is None:
        return head_b
    if head_b is None:
        return head_a
    if head_a is None and head_b is None:
        return None

    dummy = Node(0)
    curr = dummy
    curr_a = head_a
    curr_b = head_b
    while curr_a != None and curr_b != None:
        if curr_a.value < curr_b.value:
            curr.next = curr_a
            curr = curr.next
            curr_a = curr_a.next
        elif curr_a.value > curr_b.value:
            curr.next = curr_b
            curr = curr.next
            curr_b = curr_b.next
        else:
            curr.next = curr_a
            curr = curr.next
            curr_a = curr_a.next

    if curr_a == None:
        while curr_b != None:
            curr.next = curr_b
            curr = curr.next
            curr_b = curr_b.next
    if curr_b == None:
        while curr_a != None:
                curr.next = curr_a
                curr = curr.next
                curr_a = curr_a.next
    return dummy.next