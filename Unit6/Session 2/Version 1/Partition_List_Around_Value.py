'''
Problem 3: Partition List Around Value
Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(head, val):
	pass
Example Input:

# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3
Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3

plan:
1. go through the linked list and delete + store the node that >=3 in a new linked list
2. after the iteration, stick the new linked list to the back of the old linked list 
'''

'''
Understand: move all the node has value less than val to head, and node has value larger and equal to value to the tail, no sort
Plan:
- make a dummy node for list less, and a dummy node for list greater
- use while loop to scan each node:
  + if curr.value < val, add it to list less
  + if curr.value >= val, add it to list greater
- after while loop, make tail.next of list less equal to head of list greater
- return head of list less
Implement:

'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(head, val):
    less_dummy = Node(0)
    greater_dummy = Node(0)

    less_curr = less_dummy
    greater_curr = greater_dummy

    curr = head

    while curr != None:
        next_node = curr.next
        curr.next = None

        if curr.value < val:
            less_curr.next = curr
            less_curr = less_curr.next
        else:
            greater_curr.next = curr
            greater_curr = greater_curr.next

        curr = next_node
    
    less_curr.next = greater_dummy.next
    return less_dummy.next

head = Node("1", Node("4", Node("3", Node("2", Node("5", Node("2"))))))

def print_list(head):
    curr = head

    while curr is not None:
        print(curr.value, end="")
        if curr.next is not None:
            print(" -> ", end="")
        curr = curr.next

    print()

new_head = partition(head, "3")
print_list(new_head)