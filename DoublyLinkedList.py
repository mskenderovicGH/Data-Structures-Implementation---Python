# node of doubly linked list has both of neighbours as attributes
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.previous=None

# This class will implement doubly linked LinkedL
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

# if head node is present this method will insert a new node at the tail
    def insert(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

# traverse forward and backward will print out data in nodes from head or tail node
    def traverse_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node=actual_node.next

    def traverse_backward(self):
        actual_node = self.tail

        while actual_node in not None:
            print("%d" % actual_node.data)
            actual_node=actual_node.previous
