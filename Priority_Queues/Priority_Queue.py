# Priority Queue Class and examples

# Class for our Nodes 
class Node:
	# Node class constructor.
	def __init__(self, priority, value, next=None, prev=None):
		self.priority = priority
		self.value = value
		self.prev = prev
		self.next = next


# Class of List where we save all operations
class Priority_Queue:

	# Initialise the Doubly Linked List
	def __init__(self):
		# Initialise the starting state of List
		self.front = None
		self.back = None
		self.size = 0

	# Finding the lentgh of the Queue
	def len(self):
		return self.size

	# Checking if the Queue is empty
	def is_empty(self):
		if (self.size == 0):
			return True
		else:
			return False

	# Recursive function of equality ont he queue solver
	def compare_equal_sequence(self, equal_node, new_node):
		prev_node = equal_node.prev

		try:
			if (prev_node.priority == equal_node.priority):
				self.compare_equal_sequence(prev_node, new_node)
			else:
				new_node.next = prev_node.next
				new_node.prev = prev_node
				prev_node.next = new_node
				new_node.next.prev = new_node
		# If the new node placement will be at the back an error will be raised here.
		# We add a new back
		except:
			old_back_node = self.back
			self.back = new_node
			old_back_node.prev = new_node
			new_node.prev = None 
			new_node.next = old_back_node
			

	# Adding a new element in Queue
	def add(self, new_node):
		if (self.is_empty()):
			# First element in list.
			self.front = new_node
			self.back = new_node
		else:
			# Find location we need to add the element.
			temp_node = self.front
			for x in range((self.size), 0, -1):
				if (new_node.priority < temp_node.priority):
					# Change the front of Queue
					if (x == self.size):
						self.front = new_node
						new_node.next = None
					else:
						new_node.next = temp_node.next
						temp_node.next.prev = new_node
					# Default changes that happen in all positions.
					new_node.prev = temp_node
					temp_node.next = new_node
					break

				# Maybe we find equal values (can happen duplicate in queue with no limit)
				elif (temp_node.priority == new_node.priority):
					equal_node = self.compare_equal_sequence(temp_node, new_node)
					break

				# Maybe priority smallest and becomes new back
				elif (x == 1):
					new_node.prev = None
					self.back = new_node
					temp_node.prev = new_node
					new_node.next = temp_node
					break
		
				else:
					temp_node = temp_node.prev
					
		self.size = self.size + 1


	# Finding the min (Priority of element to get out of queue)
	def min(self):
		if (self.is_empty()):
			print('There is no element in the queue \n')
			return
		else:
			return self.front

	# Removing the element that has priority
	def remove_min(self):
		if (self.is_empty()):
			print('There is no element in the queue \n')
			return
		else:
			# Get the node with priority and remove
			removing_node = self.min()
			new_front = removing_node.prev
			if (new_front != None):
				self.front = new_front
				new_front.next = None
			else:
				self.front = None
				self.back = None

			self.size = self.size - 1

	# Function to display the characteristics of the Queue
	def display(self):
		if (self.is_empty()):
			print('No element in the Queue \n')
		else:
			iterator_node = self.back
			for i in range(self.size, 0, -1):
				print('Queue position: {0}, Priority : {1} , Element value {2}'.format(i, iterator_node.priority, iterator_node.value))
				iterator_node = iterator_node.next

# Driver Code
if __name__== '__main__':

	# Example nodes
	a = Node(2, 'A')
	b = Node(5, 'B')
	c = Node(1, 'C')
	d = Node(4, 'D')
	e = Node(2, 'E')
	f = Node(2, 'F')

	# Creation of queue and adding the elements
	priority_queue = Priority_Queue()
	priority_queue.add(a)
	priority_queue.add(b)
	priority_queue.add(c)
	priority_queue.add(d)
	priority_queue.add(e)
	priority_queue.add(f)

	# Displaying the Queue in the order.
	priority_queue.display()

	# Remove the first two eleemnts and add a new front
	print('We will now remove 4 elements and add a new front')
	priority_queue.remove_min()
	priority_queue.remove_min()
	priority_queue.remove_min()
	priority_queue.remove_min()
	priority_queue.add(Node(1, 'G'))

	# Displaying the Queue in the order.
	priority_queue.display()


	# Adding an new equal back and new equal back.
	print('Will add two new elements both that should be placed in the back')
	priority_queue.add(Node(5, 'H'))
	priority_queue.add(Node(6, 'I'))
	priority_queue.add(Node(6, 'J'))

	# Displaying the Queue in the order.
	priority_queue.display()

	input('Press any key to quit the session')

