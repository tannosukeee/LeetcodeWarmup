'''
Problem 4: Convert Binary Number in a Linked List to Integer
You are given the head of a linked list. Each value in the linked list is either 0 or 1, and the entire linked list represents a binary number. Return an integer that is the decimal value of the number represented by the linked list. The most significant bit is at the head of the linked list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
	pass
Example Usage:

# 1 -> 0 -> 1
num3 = Node(1)
num2 = Node(0, num3)
num1 = Node(1, num2)   # head of the list

int_num = binary_to_int(num1)
# 101 in binary is 5
print(int_num)  # Output: 5

Example Output: 5
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
	# first get length 
    n = 0
    curr = head 
    while (curr):
        n+=1
        curr= curr.next 

    res = 0
    curr = head 
    i = 0
    while(curr):
        res+=2**(n-i)*curr.value
        i+=1
    return res 

def test():
    binary = Node(1, Node(0, Node(1)))
    print(binary_to_int(binary))

test()
