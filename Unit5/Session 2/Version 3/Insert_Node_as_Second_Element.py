class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def add_second(head, val):
        if head == None or val == None:
            return None
        new_node = Node(val, head.next)
        head.next = new_node
        return head