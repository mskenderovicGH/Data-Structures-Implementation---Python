class node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

# recursive implementation of DFS
def bfs_recursive(node):

    node.visited = True
    print(node.name)

    for n in node.adjacency_list:
        if not n.visited:
            node.adjacency_list.append(n.adjacency_list)
            bfs_recursive(n)

if __name__ == '__main__':

    node1 = node("A")
    node2 = node("B")
    node3 = node("C")
    node4 = node("D")
    node5 = node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)


    dfs_recursive(node1)
