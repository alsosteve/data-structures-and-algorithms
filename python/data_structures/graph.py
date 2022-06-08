from data_structures.queue import Queue

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
        return list(self._adjacency_list.keys())

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

    def breadth_first(self, node):
        # Return: A collection of nodes in the order they were visited
        collection = []
        queue = Queue()
        visited = set()

        queue.enqueue(node)
        visited.add(node)
        while not queue.is_empty():
            check = queue.dequeue()
            collection.append(check.value)

            for neighbors in self.get_neighbors(check):
                if neighbors.vertex not in visited:
                    visited.add(neighbors.vertex)
                    queue.enqueue(neighbors.vertex)
        return collection

class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
