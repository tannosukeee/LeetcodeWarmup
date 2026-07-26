class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge_nodes(head):
    temp = Node(0)
    curr_sum = 0
    new_list_tail = temp
    
    curr = head.next
    while curr:
        if curr.value == 0:
            if curr_sum > 0:
                new_list_tail.next = Node(curr_sum)
                new_list_tail = new_list_tail.next
            curr_sum = 0
        else:
            curr_sum += curr.value
        
        curr = curr.next
    
    return temp.next