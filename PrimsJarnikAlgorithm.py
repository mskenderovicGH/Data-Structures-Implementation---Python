import heapq

class Vertex:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []


class Edge:

    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    def __lt__(self, other_edge):
        return self.weight < other_edge.weight


class PrimsJarnikAlgorithm:


    def __init__(self, unvisited_list):
        self.unvisited_list = unvisited_list
        self.mst = []
        self.total_cost = 0
        self.heap = []

    def find_spanning_tree(self, start_vertex):

        self.unvisited_list.remove(start_vertex)
        actual_vertex = start_vertex

        #iteration will go until all the verices are visited
        while self.unvisited_list:

            # consider all neighbouring edges
            for edge in actual_vertex.adjacency_list:
                # edge will be added to heap if target vertex is not visited
                if edge.target_vertex in self.unvisited_list and edge not in self.heap:
                    heapq.heappush(self.heap, edge)

            # minimum edges will be considered first
            min_edge = heapq.heappop(self.heap)

            # there still may be edges in the heap added in past iterations that lead to visited vertices so double check is necessary
            if min_edge.target_vertex in self.unvisited_list:
                self.mst.append(min_edge)
                print("Edge added to spanning tree: %s - %s" % (min_edge.start_vertex.name, min_edge.target_vertex.name))
                self.total_cost += min_edge.weight
                actual_vertex = min_edge.target_vertex
                self.unvisited_list.remove(actual_vertex)

            # this part can help to monitor edges in heap and orded of visiting vertices
            for edge in self.heap:
                print("Edge in heap: %s - %s - %s" % (edge.start_vertex.name, edge.target_vertex.name, edge.weight))
            for vertex in self.unvisited_list:
                print(vertex.name)

    def get_mst(self):
        return self.mst

    def get_total_cost(self):
        return self.total_cost


if __name__ == '__main__':

    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")
    vertexG = Vertex("G")
    vertexK = Vertex("K")

# Prims deals with undirected edges
    edgeAB = Edge(2, vertexA, vertexB)
    edgeBA = Edge(2, vertexB, vertexA)
    edgeAE = Edge(5, vertexA, vertexE)
    edgeEA = Edge(5, vertexE, vertexA)
    edgeAC = Edge(6, vertexA, vertexC)
    edgeCA = Edge(6, vertexC, vertexA)
    edgeAF = Edge(10, vertexA, vertexF)
    edgeFA = Edge(10, vertexF, vertexA)
    edgeBE = Edge(3, vertexB, vertexE)
    edgeEB = Edge(3, vertexE, vertexB)
    edgeBD = Edge(3, vertexB, vertexD)
    edgeDB = Edge(3, vertexD, vertexB)
    edgeCD = Edge(1, vertexC, vertexD)
    edgeDC = Edge(1, vertexD, vertexC)
    edgeCF = Edge(2, vertexC, vertexF)
    edgeFC = Edge(2, vertexF, vertexC)
    edgeDE = Edge(4, vertexD, vertexE)
    edgeED = Edge(4, vertexE, vertexD)
    edgeDG = Edge(5, vertexD, vertexG)
    edgeGD = Edge(5, vertexG, vertexD)
    edgeFG = Edge(5, vertexF, vertexG)
    edgeGF = Edge(5, vertexG, vertexF)
    edgeGK = Edge(10, vertexG, vertexK)
    edgeKG = Edge(10, vertexK, vertexG)

    unvisited_list = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF, vertexG, vertexK]

    vertexA.adjacency_list.append(edgeAB)
    vertexA.adjacency_list.append(edgeAC)
    vertexA.adjacency_list.append(edgeAE)
    vertexA.adjacency_list.append(edgeAF)
    vertexB.adjacency_list.append(edgeBA)
    vertexB.adjacency_list.append(edgeBD)
    vertexB.adjacency_list.append(edgeBE)
    vertexC.adjacency_list.append(edgeCA)
    vertexC.adjacency_list.append(edgeCD)
    vertexC.adjacency_list.append(edgeCF)
    vertexD.adjacency_list.append(edgeDB)
    vertexD.adjacency_list.append(edgeDC)
    vertexD.adjacency_list.append(edgeDE)
    vertexD.adjacency_list.append(edgeDG)
    vertexE.adjacency_list.append(edgeEA)
    vertexE.adjacency_list.append(edgeEB)
    vertexE.adjacency_list.append(edgeED)
    vertexF.adjacency_list.append(edgeFA)
    vertexF.adjacency_list.append(edgeFC)
    vertexF.adjacency_list.append(edgeFG)
    vertexG.adjacency_list.append(edgeGD)
    vertexG.adjacency_list.append(edgeGF)
    vertexG.adjacency_list.append(edgeGK)
    vertexK.adjacency_list.append(edgeKG)

    algorithm = PrimsJarnikAlgorithm(unvisited_list)
    algorithm.find_spanning_tree(vertexA)
    print(algorithm.get_total_cost())
