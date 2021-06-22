# class Vertex will represent vertices ing the original graph
class Vertex:

    def __init__(self, name):
        self.name = name
        self.node = None


class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

# less than function is overidden because Kruskal needs to sort the edges by weight
    def __lt__(self, other_edge):
        return self.weight < other_edge.weight


# class Node will represent tree nodes of the disjoint sets
class Node:

    def __init__(self, rank, node_id, parent=None):
        self.rank = rank
        self.node_id = node_id
        self.parent = parent


class DisjointSet:

    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.root_nodes = []
        # for every vertex single node disjoint sets is made
        self.make_sets()

    # find function will return disjoint set representative / root node
    def find(self, node):

        current_node = node

        while current_node.parent is not None:
            current_node = current_node.parent

    # path compression can be done so the next time find method is called it will be executed in O(1)
    # all nodes will point to the root node
        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent
            current_node.parent = root
            current_node = temp

        return root.node_id

    def merge(self, node1, node2):

        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return

    # two disjoint sets will be merged according to the rank of their representatives

        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]

        if root1.rank < root2.rank:
            root1.parent = root2
        elif root1.rank > root2.rank:
            root2.parent = root1
        else:
            root2.parent = root1
            root1.rank = root1.rank + 1

    def make_sets(self):
        for v in self.vertex_list:
            node = Node(0, len(self.root_nodes))
            v.node = node
            self.root_nodes.append(node)


class KruskalAlgorithm:

    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def find_mst(self):

        disjoint_set = DisjointSet(self.vertex_list)
        mst = []

        # edges will be considered in the sorted order
        self.edge_list.sort()

        for edge in self.edge_list:

            u = edge.start_vertex
            v = edge.target_vertex

        # Kruskal will merge all vertices in one set using the shortest edges 
            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                mst.append(edge)
                disjoint_set.merge(u.node, v.node)

        for edge in mst:
            print(edge.start_vertex.name, " - ", edge.target_vertex.name, " - ", edge.weight)


if __name__ == '__main__':

    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")

    edge1 = Edge(2, vertex1, vertex2)
    edge2 = Edge(6, vertex1, vertex3)
    edge3 = Edge(5, vertex1, vertex5)
    edge4 = Edge(10, vertex1, vertex6)
    edge5 = Edge(3, vertex2, vertex4)
    edge6 = Edge(3, vertex2, vertex5)
    edge7 = Edge(1, vertex3, vertex4)
    edge8 = Edge(2, vertex3, vertex6)
    edge9 = Edge(4, vertex4, vertex5)
    edge10 = Edge(5, vertex4, vertex7)
    edge11 = Edge(5, vertex6, vertex7)

    vertices = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7]
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11]

    algorithm = KruskalAlgorithm(vertices, edges)
    algorithm.find_mst()
