from vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        # store all vertices connected to the instance
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding {}".format(vertex.value))
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex):
        print("Adding edge from {0} to {1}".format(from_vertex.value, to_vertex.value))
        self.graph_dict[from_vertex.value]
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
        if self.directed == False:
            self.graph_dict[to_vertex.value]


self.graph_dict[to_vertex.value].add_edge(from_vertex.value)


grand_central = Vertex("Grand Central Station")


railway = Graph()
print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)
