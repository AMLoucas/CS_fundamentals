# Class for our Nodes 
class Node:
	# Node class constructor.
	def __init__(self, value=None, next=None, prev=None):
		self.value = value
		self.prev = prev
		self.next = next


# Class of List where we save all operations
class DoublyLinkedList:

	# Initialise the Linked List
	def __init__(self):
		# Initialise the starting state of List
		self.head = None
		self.tail = None
		self.size = 0

	# Get the value of the index asked for:
	def get(self, index):
		# Condition if index is valid
		if index < 0 or index >= self.size:
			print('Index position is out of bounds.')
			return -1

		# Getting the first element
		current_position = self.head

		# Traversing list until element obtained
		while index != 0:
			current_position = current_position.next
			index -= 1

		return current_position.value

	# Add a node to the head position
	def addHead(self, value):
		# Create a new node to add in List
		node = Node(value)

		# Checking if head already exists or not.
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node

		# List size has increased
		self.size += 1 

	# Add a node to the tail position
	def addTail(self, value):
		# Create a new node to add in List
		node = Node(value)

		# Checking if tail already exists or not.
		if self.tail is None:
			self.head = node
			self.tail = node
		else:
			node.prev = self.tail
			self.tail.next = node
			self.tail = node

		# List size has increased
		self.size += 1

	# Add a node to specific location
	def addAtIndex(self, index, value):
		# Checking the index of new value.
		# Maybe user trying to add on head or tail or out of bounds.
		if index < 0 or index > self.size:
			print('Index position is out of bounds.')
			return None
		# New head
		elif index == 0:
			self.addHead(value)
		# New tail
		elif index == self.size:
			self.addTail(value)
		# New addition in middle
		else:
			# Getting the first element
			current_position = self.head

			# Traversing list until element obtained
			while ((index-1) != 0):
				current_position = current_position.next
				index -= 1

			node = Node(value)

			# Reshaping the list.
			node.next = current_position.next
			current_position.next.prev = node
			current_position.next = node
			node.prev = current_position

			# List size has increased
			self.size += 1 

	def deleteAtIndex(self, index):
		# Checking the index of new value.
		# Maybe user trying to add on head or tail or out of bounds.
		if index < 0 or index >= self.size:
			print('Index position is out of bounds.')
			return None
		#
		# Deleting head
		elif index == 0:
			existing_node = self.head.next
			if existing_node:
				existing_node.prev = None

			self.head = self.head.next
			self.size -= 1

			# Code had an error here (I think)
			if self.size == 0:
				self.tail = self.head
		#
		# Deleting tail
		elif index == self.size-1:
			existing_node = self.tail.prev
			if existing_node:
				existing_node.next = None

			self.tail = self.tail.prev
			self.size -= 1

			# Code had an error here (I think)
			if self.size == 0:
				self.head = self.tail
		#
		# New deletion in middle
		else:
			# Getting the first element
			current_position = self.head

			# Traversing list until element obtained
			while ((index-1) != 0):
				current_position = current_position.next
				index -= 1

			# Reshaping the list.
			current_position.next = current_position.next.next
			current_position.prev = current_position
			
			# List size has increased
			self.size -= 1

	# Reverse the sequence of the list
	def reverseOrderList(self):
		# initialize variables -> we need values for three of them.
		previous = None         
		current = self.head     
		following = current.next

		# Updating the tail
		self.tail = current

		# loop through list to change the order of linkage.
		while current:
			current.next = previous
			previous = current      
			current = following
			if following:
				following = following.next

			self.head = previous

	# Print List
	def printList(self):
		print('The current state of the linked list is : ')

		i = 0
		while (i != self.size):
			node = self.get(i)
			print(f' At index: {i} we have the value : {node}')
			i += 1

	def initialise_list(self, nums):
		# Initialising the list with users values
		self.addHead(nums[0])
		nums = nums[1:]
		for num in nums:
			self.addTail(num)

		return self



'''
Main code of a test run of the above and validating if correct.
'''
# List creation
print('Creating list ... ')
nums = [3, 4, 5, 6, 7, 8, 9]
LL = DoublyLinkedList()
LL.initialise_list(nums)


# Printing the list.
print('List is created!')
LL.printList()

# Removing element at index 1 -> Number 4
LL.deleteAtIndex(1)
print('Deleting element at index 1 -> Value 4 removed')
LL.printList()

# Adding element at index 3
print('Adding element at index 3 -> value 11')
LL.addAtIndex(3, 11)
LL.printList()

# Adding a new head using index add
print('Adding new element at HEAD position -> value 20')
LL.addAtIndex(0, 20)
LL.printList()

# Reversing the lists order
print('Reversing the order of the list')
LL.reverseOrderList()
LL.printList()



# Keep window open until user wants to exit
input("Quit the application by pressing key 'ENTER'")