class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_dupes(head):
    dummy = Node(0, head)
    prev = dummy
    curr = head

    while curr is not None:
        duplicate = False

        while curr.next is not None and curr.value == curr.next.value:
            duplicate = True
            curr = curr.next

        if duplicate:
            prev.next = curr.next
        else:
            prev = prev.next

        curr = curr.next

    return dummy.next

def print_list(head):
    curr = head

    while curr is not None:
        print(curr.value, end="")
        if curr.next is not None:
            print(" -> ", end="")
        curr = curr.next

    print()

node6 = Node(5)
node5 = Node(4, node6)
node4 = Node(3, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
head = Node(1, node2)

new_head = delete_dupes(head)
print_list(new_head)
