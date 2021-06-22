# Class node will define an element inside of binary search tree
class Node:

# Every node has data, parent (initialized by constructor), left and right child (None by default)
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

# This class implements binary search tree structure
class BinarySearchTree:

    def __init__(self):
        self.root = None

# New node will be inserted as a tree leaf
    def insert(self,data):
        if self.root is None:
            self.root = Node(data,None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if data<node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        else:
            if node.rightChild:
                self.insert_node(data,node.rightChild)
            else:
                node.rightChild=Node(data,node)


    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

# max data in the tree is rightmost leaf
    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        else:
            return node.data
# min data in the tree is leftmost leaf
    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        else:
            return node.data

# traverse will print from the leftmost tree to the rightmost tree
    def traverse_in_order(self,node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print('%s' % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)


# To remove data will have to find the node in the tree and then reorder the tree accordingly before deleting it

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)


    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:
            if node.leftChild is None and node.rightChild is None:
                print("Removing a leaf node ... %d" % node.data)

                parent = node.parent

                if parent is not None and parent. leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.rightChild is None and node.leftChild is not None:
                print ("Removing a node with single left child ...")

                parent = node.parent

                if parent is not None:
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                else:
                    self.root = node.leftChild

                node.leftChild.parent = parent
                del node

            elif node.leftChild is None and node.rightChild is not None:
                print ("Removing a node with single right child ...")

                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            else:
                print(' Removing node with two children...')

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        return node




bst = BinarySearchTree()
bst.insert(10)
bst.insert(7)
bst.insert(66)
bst.insert(-1)
bst.insert(33)
bst.insert(22)
bst.insert(1)


print(bst.get_max_value())
print('_______________')
print(bst.get_min_value())
print('_______________')
bst.remove(33)
bst.traverse()
