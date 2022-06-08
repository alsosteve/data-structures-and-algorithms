# from data_structures.graph import Graph

def direct_flights(graph, names):
    # return the weight between two connected nodes

    weight = 0

    for i in range(len(names)-1):
        start = names[i]
        end = names[i+1]

        # find start node
        for node in graph.get_nodes():
            if node.value == start:

                # if start is connected to end
                for edge in graph.get_neighbors(node):
                    if edge.vertex.value == end:
                        weight += edge.weight

    # returns
    if weight == 0: return False, weight
    else: return True, weight
