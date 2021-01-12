#Circular Linked List

class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.value = value
		self.next = None

class Circular_LinkedList(object):
	"""docstring for Circular_LinkedList"""
	def __init__(self):
		self.head = None
		self.tail = None
		
	def create_Circular_LL(self, value):
		new_node = Node(value)
		if self.head is None:
			new_node.next = new_node
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.tail.next = new_node
			self.tail = new_node

	def add_by_index(self, value, index):
		new_node = Node(value)
		i = 0
		current_node = self.head
		previous_node = None
		if self.head == None:
			new_node.next = new_node
			self.head = new_node
			self.tail = new_node
		else:
			while i < index and current_node.next != None:
				previous_node = current_node
				current_node = current_node.next
				i += 1
			if i == index:
				#if 
				previous_node.next = new_node
				new_node.next = current_node
				return True
				
	def to_list(self):
		lst = []
		checking_node = self.head
		if self.head is None:
			return 'The linkes list does not exist'
		else:
			while checking_node != None:
				lst.append(checking_node.value)
				if checking_node.next != self.head:
					checking_node = checking_node.next
				else:
					return lst
		return lst

CSLL = Circular_LinkedList()
CSLL.create_Circular_LL(1)
CSLL.create_Circular_LL(2)
CSLL.create_Circular_LL(3)
CSLL.create_Circular_LL(4)
CSLL.create_Circular_LL(5)
CSLL.create_Circular_LL(6)
CSLL.add_by_index('a', 7)
CSLL.add_by_index('b', 3)


print(CSLL.to_list())