class vertex:
    def __init__(self, n):
        self.name = n
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            self.adjacent_vertices.sort()


class graph:
    vertices = {}

    def add_vertex(self, a_vertex):
        if isinstance(a_vertex, vertex) and a_vertex.name not in self.vertices:
            self.vertices[a_vertex.name] = a_vertex
            return True
        else:
            return False
        
    def add_edge(self, a_vertex, another_vertex):
        if a_vertex in self.vertices and another_vertex in self.vertices:
            for key, value in self.vertices.items():
                if key == a_vertex:
                    value.add_adjacent_vertex(another_vertex)
                if key == another_vertex:
                    value.add_adjacent_vertex(a_vertex)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice " + key + " - adyacentes: " + str(self.vertices[key].adjacent_vertices))


if __name__ == "__main__":
    my_graph = graph()
    my_vtx = vertex('A')
    my_graph.add_vertex(my_vtx)

    for i in range(ord('A'), ord('K')):
        my_graph.add_vertex(vertex(chr(i)))
    
    edges = ['AB', 'AE', 'BF', 'CG','DE','DH','EH','FG','FI','FJ','GJ']

    for edge in edges:
        my_graph.add_edge(edge[:1],edge[1:])
    
    my_graph.print_graph()