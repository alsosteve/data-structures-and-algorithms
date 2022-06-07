class Graph:
    """
    A graph method
    """

    def __init__(self):
        # initialization here
        self._adjacency_list = {}

    def add_node(self, value):
        # adds node to graph
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def size(self):
        # Returns the total number of nodes in the graph
        return len(self._adjacency_list)

    def get_nodes(self):
        # Returns all of the nodes in the graph as a collection
        return self._adjacency_list.keys()

    def add_edge(self, start_vertex, end_vertex, weight=0):
        # Adds a new edge between two nodes
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError()

        edge = Edge(end_vertex, weight)

        list_of_edges = self._adjacency_list[start_vertex]

        list_of_edges.append(edge)

    def get_neighbors(self, vertex):
        # Returns a collection of edges connected to a given node
        return self._adjacency_list[vertex]

class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
