class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())


grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

    def add_edge(self, vertex):
        print("Adding edge to {}".format(vertex))
        self.edges[vertex] = True
