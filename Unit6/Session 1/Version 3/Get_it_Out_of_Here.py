class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Function with a bug!
def remove_by_value(head, val):
    # Handle empty list and removal from the head
    if not head:
        return None
    if head.value == val:
        return head.next  # Return the second node as the new head

    current = head
    while current.next:
        if current.next.value == val:
            current.next = current.next.next  # Skip the node with the value
            return head  # Return the original head
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
head = Node(1, node2)

print_list(head)

head = remove_by_value(head, 3)

print_list(head)