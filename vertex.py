class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        # self.edges[vertex] is corresponding edge's value
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())
