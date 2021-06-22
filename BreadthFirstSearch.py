# BFS will go through the tree according to FIFO
class Node:

    def __init__(self,name):
        self.name = name
        self.adjecency_list = []
        self.visited = False

def breadth_first_search(start_node):

    queue = [start_node]

    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)
        for n in actual_node.adjecency_list:
            if not n.visited:
                queue.append(n)

if __name__ == '__main__':

    node1 = Node("London")
    node2 = Node("Berlin")
    node3 = Node("NewYork")
    node4 = Node("Madrid")
    node5 = Node("Sarajevo")

    node1.adjecency_list.append(node5)
    node1.adjecency_list.append(node3)
    node3.adjecency_list.append(node4)
    node5.adjecency_list.append(node2)

    breadth_first_search(node1)
