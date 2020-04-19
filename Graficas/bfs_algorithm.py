class vertex:
    def __init__(self, n):
        self.name = n
        self.adjacent_vertices = []
        self.distance = 9999
        self.color = 'white'
        self.predecesor = -1

    def add_adjacent_vertex(self, vertex):
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            self.adjacent_vertices.sort()


class graph:
    vertices = {}
    exploration_order = []

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
    
    def bfs(self, a_vertex):
        a_vertex.distance = 0
        a_vertex.color = 'gray'
        a_vertex.predecesor = -1
        q = []
        q.append(a_vertex.name)
        self.exploration_order.append(a_vertex.name)

        while len(q) > 0:
            u = q.pop()
            node_u = self.vertices[u]
            for v in node_u.adjacent_vertices:
                node_v = self.vertices[v]
                if node_v.color == 'white':
                    node_v.color = 'gray'
                    self.exploration_order.append(node_v.name)
                    node_v.distance = node_u.distance + 1
                    node_v.predecesor = node_u.name
                    q.append(v)
            self.vertices[u].color = 'black'

    def print_graph_bfs(self):
        for key in sorted(list(self.vertices.keys())):
            print("La distancia de A a " + key + " es: " + str(self.vertices[key].distance))
        print("\nDescubimiento de los nodos: ", self.exploration_order)


if __name__ == "__main__":
    my_graph = graph()
    my_vtx = vertex('A')
    my_graph.add_vertex(my_vtx)

    for i in range(ord('A'), ord('I')):
        my_graph.add_vertex(vertex(chr(i)))
    
    edges = ['AB', 'AC', 'BD', 'BE','CF','CG','CH']

    for edge in edges:
        my_graph.add_edge(edge[:1],edge[1:])
    
    my_graph.print_graph()
    my_graph.bfs(my_vtx)
    my_graph.print_graph_bfs()