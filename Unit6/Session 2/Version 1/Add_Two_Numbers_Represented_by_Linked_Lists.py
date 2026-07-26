class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_two_numbers(head_a, head_b):
    if head_a == None or head_b == None:
        return None
    dummy = Node(0)
    curr_dummy = dummy
    curr_a = head_a
    curr_b = head_b
    carry = 0
    while curr_a or curr_b or carry > 0:
        value_a = curr_a.value if curr_a else 0
        value_b = curr_b.value if curr_b else 0

        total = value_a + value_b + carry

        curr_dummy.next = Node(total % 10)

        curr_dummy = curr_dummy.next

        carry = total // 10

        if curr_a:
            curr_a = curr_a.next
        if curr_b:
            curr_b = curr_b.next
    return dummy.next

def print_list(head):
    curr = head

    while curr:
        print(curr.value, end="")
        if curr.next:
            print(" -> ", end="")
        curr = curr.next

    print()

# 2 -> 4 -> 3 represents 342
head_a = Node(2, Node(4, Node(3)))

# 5 -> 6 -> 4 represents 465
head_b = Node(5, Node(6, Node(4)))

result = add_two_numbers(head_a, head_b)
print_list(result)