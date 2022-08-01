'''
We will implement a Queue using a Linked List as the main data structure
There are other ways to implement a Queue:
- Simple List (Array)
- Libraries
'''

# Node class that holds data for each element inside.
class Node:
      
    def __init__(self, data):
        self.data = data
        # next shows to new element in queue
        self.next = None
  
# Queue class that holds a collection of the nodes in a queue logic.
class Queue:
    
    # Constructor
    def __init__(self):
        self.front = None
        self.back = None
  
    # Checking if queue is empty
    def is_empty(self):
        return self.front == None
    
    # See the first element of the queue
    def peek_front(self):
        if self.is_empty():
            print('No elements in Queue')
        else:
            print('Element in front is', self.front.data)
    
    # See the last element of the queue
    def peek_back(self):
        if self.is_empty():
            print('No elements in Queue')
        else:
            print('Element in front is', self.back.data)


    # Method to add an item to the queue
    def en_queue(self, data):
        adding_node = Node(data)
          
        if self.back == None:
            self.front = adding_node
            self.back = adding_node
        else:
            # Existing node points to new node.
            self.back.next = adding_node
            # New node becoming the new back.
            self.back = adding_node
  
    # Method to remove an item from queue
    def de_queue(self):
        if self.is_empty():
            return
        
        removing_node = self.front
        # Removing the node.
        self.front = removing_node.next
        # If no more elements removing the back node pointer.
        if(self.front == None):
            self.back = None

    # Prints out the queue     
    def print_queue(self):
        if self.is_empty():
            print("Your queue is empty, please add elements.")
        else:
            # Iterating through stack to print the status.
            iterator_node = self.front
            print('Current Queue status is: \n')
            while(iterator_node != None):
                print(iterator_node.data, "\n")
                iterator_node = iterator_node.next
            return
  
# Driver Code
if __name__== '__main__':
    ###
    # Creating a queue.
    Queue = Queue()
    ###
    # Adding elements.
    Queue.en_queue(10)
    Queue.en_queue(20)
    Queue.en_queue(30)
    Queue.en_queue(40)
    Queue.en_queue(50) 

    # Printing our the queue.
    Queue.print_queue()
    # Printing front and back
    Queue.peek_front()
    Queue.peek_back()

    ###
    # Removing two elements.
    Queue.de_queue()
    Queue.de_queue()

    # Printing out the queue.
    Queue.print_queue()
    # Printing front and back
    Queue.peek_front()
    Queue.peek_back()
