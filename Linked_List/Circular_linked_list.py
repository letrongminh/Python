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
	def traversal(self):
		current_node = self.head
		if self.head == None:
			return "the linked list does not exist"
		else:
			while current_node.next != None:
				print(current_node.value)
				current_node = current_node.next
				if current_node == self.tail.next: # prevent infinite loops 
					break



	def searching(self, value_seaching):
		if self.head == None:
			return "the linked list does not exist"
		else:
			current_node = self.head
			i = 0
			while current_node.next != None:
				if current_node.value == value_seaching:
					print('in this linked-list does exist value', value_seaching, 'at index', i)
				current_node = current_node.next
				i += 1
				if current_node == self.tail.next:
					break

	def delete(self, index):
		if self.head ==None: 
			return "the linked list does not exist"
		else:
			i = 0
			current_node = self.head
			previous_node = None
			while i < index and current_node.next:
				previous_node = current_node
				current_node = current_node.next
				i+=1
			if i == index:
				if current_node.next == None: #checking here: self.head == self.tail ?
					self.head = None
					self.tail = None
				else:
					previous_node.next = current_node.next
					#current_node = current_node.next
			if current_node == self.tail.next:
				self.tail = previous_node
				previous_node.next = self.head

	def delete_val(self, value_del):

		if self.head ==None: 
			return "the linked list does not exist"
		else:
			current_node = self.head
			previous_node = None
			while current_node.next != None:
				if current_node.value == value_del:
					if current_node.next == None: #checking here: self.head == self.tail ?
						self.head = None
						self.tail = None
						break # if without break in the code, the loop is infinite
					else:
						previous_node.next = current_node.next
						break # if without break in the code, the loop is infinite
				if current_node == self.tail:
					self.tail = previous_node
					previous_node.next = self.head
					break # if without break in the code, the loop is infinite
				previous_node = current_node
				current_node = current_node.next
	def delete_entire(self):
		if self.head == None:
			print('The Linked List does not exist')
		else:
			self.head = None
			self.tail = None

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

CSLL.traversal()
CSLL.searching(4)
print('_________')
CSLL.delete(7)
print('delete index = 7 in the linked list:', CSLL.to_list())

print('_________')

CSLL.delete_val(4)
print('delete  value 4 in the linked list:', CSLL.to_list())
