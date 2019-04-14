# jalyxis
# Project 5 - Hash Table
# Spring 2019
# Algorithm Design and Analysis

# Linked List Class

# Node class for each element in a linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Linked List class
class LList:
    def __init__(self):
        self.head = None

    # Print Linked List
    def printLList(self):
        val = self.head
        while val is not None:
            print(val.data)
            val = val.next

    # Insert value at beginning of list
    def insertFront(self, newData):
        newNode = Node(newData)

        # Update newNode.next to point to old head
        newNode.next = self.head
        self.head = newNode

    # Append value to end of list
    def appendLList(self, newData):
        newNode = Node(newData)

        # If LList is empty
        if self.head is None:
            self.head = newNode
            return
        
        end = self.head

        # Traverse list until end and append newNode
        while(end.next):
            end = end.next
        end.next = newNode

    # Insert value between existing nodes
    def insertLList(self, middle, newData):
        # if node to insert behind does not exist
        if middle is None:
            print("The mentioned node is absent.")
            return

        # Found node to insert behind
        newNode = Node(newData)
        newNode.next = middle.next
        middle.next = newNode

    # Remove a node from the list
    def remove(self, key):
        headVal = self.head

        if(headVal is not None):
            if(headVal.data == key):
                self.head = headVal.next
                headVal = None
                return

        while(headVal is not None):
            if(headVal.data == key):
                break
            prev = headVal
            headVal = headVal.next

        if(headVal == None):
            return

        prev.next = headVal.next

        headVal = None
