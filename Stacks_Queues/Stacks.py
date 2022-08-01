'''
We will implement a Stack using a Linked List as the main data structure
There are other ways to implement a Stack:
- Simple List (Array)
- Libraries
'''

# Node class that holds data for each element inside.
class Node:

    # Constructor of the node.
    def __init__(self,data):
        self.data = data
        # Next is a pointer to the next already added elements.
        self.next = None

# Class the holds and relates all the nodes together in a Stack logic.
class Stack:
    
    def __init__(self):
        self.head = None
      
    # If no head exists than the Stack is empty. 
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
      
    # Add a new element in the stack
    def push(self,data):
        if self.is_empty():
            self.head=Node(data)
        else:
            added_node = Node(data)
            # Adding pointer to already existing element and changing head.
            added_node.next = self.head
            self.head = added_node
      
    # Remove element -> Can only remove the head.
    def pop(self):
        if self.is_empty():
            return None
        else:
            removing_node = self.head
            # preceeding node.
            self.head = self.head.next
            # removing node and returing the data value.
            removing_node.next = None
            return removing_node.data
      
    # Returns the head node data
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
      
    # Prints out the stack     
    def print_stack(self):
        if self.is_empty():
            print("Your stack is empty, please add elements.")
        else:
            # Iterating through stack to print the status.
            iterator_node = self.head
            print('Current Stack status is: \n')
            while(iterator_node != None):
                print(iterator_node.data, "\n")
                iterator_node = iterator_node.next
            return

    # Calculating the length of the stack
    def len(self):
        if self.is_empty():
            print("Your stack is empty, please add elements.")
        else:
            # Iterating through stack to get number of elements.
            iterator_node = self.head
            counter = 0 
            while(iterator_node != None):
                counter = counter + 1
                iterator_node = iterator_node.next

            return counter


if __name__ == "__main__" :        
    # Initialising our stack.
    MyStack = Stack()
    ###
    # Adding elements in our stack
    MyStack.push('Green') 
    MyStack.push('Blue')
    MyStack.push('Red')
    MyStack.push('Orange')
    MyStack.push('Yellow')
    
    # Display stack elements 
    MyStack.print_stack()
    print('Number of element\'s in the stack: ', MyStack.len())
    
    # Print top element of stack 
    print("\n Top element is ",MyStack.top())
    ###
    # Removing two elements elements of stack 
    MyStack.pop()
    MyStack.pop()
    
    # Display stack elements
    MyStack.print_stack()
    print('Number of element\'s in the stack: ', MyStack.len())

    # Print top element of stack 
    print("\nTop element is ", MyStack.top()) 
    ###
    # Adding a new element
    MyStack.push('Purple')

    # Display stack elements
    MyStack.print_stack()
    print('Number of element\'s in the stack: ', MyStack.len())

    # Print top element of stack 
    print("\nTop element is ", MyStack.top()) 

    # Just placeholder to not close terminal.
    input("Press any key to quit the data structure.")