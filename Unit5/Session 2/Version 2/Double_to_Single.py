class SLLNode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class DLLNode:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def dll_to_sll(dll_head):
	if dll_head == None:
		return None
	sll_head = SLLNode(dll_head.value)
	sll_curr = sll_head
	dll_curr = dll_head.next
	while dll_curr != None:
		new_node = SLLNode(dll_curr.value)
		sll_curr.next = new_node
		sll_curr = sll_curr.next
		dll_curr = dll_curr.next
	return sll_head

ice = DLLNode("Ice")
water = DLLNode("Water")
steam = DLLNode("Steam")

ice.next = water
water.prev = ice
water.next = steam
steam.prev = water

sll_head = dll_to_sll(ice)