class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def get_length(node):
    if node == None:
        return None
    curr_next = node
    curr_prev = node.prev
    count_next = 0
    count_prev = 0
    while curr_next != None:
        count_next += 1
        curr_next = curr_next.next
    while curr_prev != None:
        count_prev += 1
        curr_prev = curr_prev.prev
    return count_next + count_prev
