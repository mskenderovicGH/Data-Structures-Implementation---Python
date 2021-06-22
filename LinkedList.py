# Class Node will define an element inside of a linked list
class Node:
# Class constructor will accept and assign data to the Node,
# next node in linked list is None by default
    def __init__(self, data):
        self.data=data
        self.nextNode=None

# This class will order many Node objects into a LinkedList
# and it will hold information about the head node and number of nodes in the list
class LinkedList:

    def self__init(self):
        self.head=None
        self.numOfNodes=0

# This method will assign a new node to the head node
    def insert_start(self,data)

        self.numOfNodes = self.numOfNodes+1
        new_node=Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode=self.head
            self.head=new_node

# This method will assign a new node to the end of the list
    def insert_end(self_data):

        self.numOfNodes = self.numOfNodes+1
        new_node = Node(data)

        actual_node = self.head
        while actual_node.nextNode is not None:
            actual_node=actual_node.nextNode

        actual_node.nextNode = new_node

# Method returns the number of nodes in the linked list
    def size_of_linkedlist(self):
        return self.numOfNodes

# Method prints out data of all nodes in the list
    def traverse(self):
        actual_node=self.head

        while actual_node not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

# Method removes a node with certain data from the linked list
    def remove(self,data):
        if self.head is None:
            return
        actual_node = self.head
        previous_node = None

        while actual_node in not None and actual_node.data!=data:
            previous_node=actual_node
            actual_node = actual_node.nextNode

        if actual_node is None:
            return

        self.numOfNodes=self.numOfNodes-1

# removal is done by reassigning the next node attribute
        if previous_node is None:
            self.head = actual_node.nextNode
        else
            previous_node.nextNode = actual_node.nextNode
