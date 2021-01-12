#create a linkied list
#single linked list
#Node
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
class Singly_LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	'''def __iter__(self):
		checking = self.head
		while checking:
			yield checking
			checking = checking.next'''

	def add(self, add_value):
		new_node = Node(add_value)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	def add_by_index(self, add_value, index):
		new_node = Node(add_value)
		previous_node = None
		currently_node = self.head
		i = 0
		'''if self.head is None:
			self.head = new_node
			self.tail = new_node
		'''
		while i < index and currently_node.next:
			previous_node = currently_node
			currently_node = currently_node.next
			i += 1
		print(i)
		if i == index :
			previous_node.next = new_node
			new_node.next = currently_node
			'''
			new_node.next = None #create link for new_node 
			self.tail.next = new_node #create link for tail to new_node
			self.tail = new_node # assign value new_node for tail
			'''
			return True
		else: 
			return False

	def to_list(self):
		list_1=[]
		node_checking = self.head
		while node_checking:
			list_1.append(node_checking.value)
			node_checking = node_checking.next
		return list_1

	def traverse(self):
		if self.head is None:
			print('not exist')
		else:
			currently_node = self.head
			while currently_node != None:
				print(currently_node.value)
				currently_node = currently_node.next

	def searching(self, seaching_value):
		if self.head is None:
			print('not exist')
		else:
			currently_node = self.head
			while currently_node != None:
				if currently_node.value == seaching_value: #Currently_node gets the value, then compares it with the seaching_value
					return 'this value seaching exist in this linked list'
				currently_node = currently_node.next

			return 'not exist in this Linked list'

	def delete_node(self, index): #delete follow location
		i = 0
		currently_node = self.head
		previous_node = None
		if self.head is None:
			return 'not exist Linked List'
		else:
			if index == 0:
				if currently_node.next != None:
					self.head = self.head.next
				else:
					self.head = None
					self.tail = None

			while i < index and currently_node.next != None:

				#currently_node = currently_node.next.next
				previous_node = currently_node
				currently_node = currently_node.next
				i += 1
			if i == index and index != 0:
				previous_node.next = currently_node.next
				return True

	def delete_value(self, delete_value): #delete if value matching
		currently_node = self.head
		previous_node = None
		if self.head is None:
			return 'not exist Linked List'
		else:
			while currently_node != None:
				if currently_node.value == delete_value:
					if previous_node != None:
						previous_node.next = currently_node.next
					else:
						self.head = self.head.next
					return True
				previous_node = currently_node
				currently_node = currently_node.next

	#delete entire Linked List
	def delete_entire(self):
		if self.head == None:
			print('The Linked List does not exist')
		else:
			self.head = None
			self.tail = None

test1 = Singly_LinkedList()
test1.add(1)
test1.add(2)
test1.add(3)
test1.add(4)
test1.add_by_index(5, 2)
#print([checking.value for checking in test1])
print(test1.to_list())
test1.traverse()
print(test1.searching(3))

print('__________')

test1.delete_node(3)
print(test1.to_list())

print('__________')

test1.delete_value(4)
print(test1.to_list())

print('__________')

test1.delete_entire()
print(test1.to_list())
