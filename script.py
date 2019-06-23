from vertex import Vertex

from graph import Graph

railway = Graph()

station_one = Vertex("Ballahoo")
station_two = Vertex("Penn")


railway.add_vertex(station_one)
railway.add_vertex(station_two)


railway.add_edge(station_one, station_two)
print("Edges for {0}: {1}".format(station_one.value, station_one.get_edges()))
print("Edges for {0}: {1}".format(station_two.value, station_two.get_edges()))
