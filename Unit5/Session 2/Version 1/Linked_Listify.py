class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_to_linked_list(lst):
    head = Node(lst[0])
    curr = head
    for i in range(1, len(lst)):
        n = Node(lst[1])
        curr.next = n
        curr = n
    return head

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)


# This prints ONLY the head node's value:
print(linked_list.value)   # => "Betty"

# (Optional) Traverse to print the whole linked list:
current = linked_list
while current:
    end_arrow = " -> " if current.next else "\n"
    print(current.value, end=end_arrow)
    current = current.next


# Print the head node's VALUE:
print(linked_list.value)        # expected: Betty