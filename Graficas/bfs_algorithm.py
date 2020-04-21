class vertex:
    def __init__(self, n):
        self.name = n
        self.adjacent_vertices = []
        self.distance = 9999
        self.color = 'white'
        self.predecessor = -1

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
            return True
        else:
            return False

    def print_graph(self):
        for key in list(self.vertices.keys()):
            print("Vertice " + key + " - adyacentes: " + str(self.vertices[key].adjacent_vertices))
        print("\n")
        
    def bfs(self, a_vertex):
        a_vertex.distance = 0
        a_vertex.color = 'gray'
        a_vertex.predecessor = -1
        q = []
        q.append(a_vertex.name)

        while len(q) > 0:
            u = q.pop(0)
            self.exploration_order.append(u)
            current_vrtx = self.vertices[u]
            
            for v in current_vrtx.adjacent_vertices:
                adj_vrtx = self.vertices[v]
                
                if adj_vrtx.color == 'white':
                    adj_vrtx.color = 'gray'
                    adj_vrtx.distance = current_vrtx.distance + 1
                    adj_vrtx.predecessor = current_vrtx.name
                    q.append(v)
            self.vertices[u].color = 'black'

    def print_graph_bfs(self):
        for key in sorted(list(self.vertices.keys())):
            print("La distancia de A a " + key + " es: " + str(self.vertices[key].distance))
        print("\nDescubimiento de los nodos: ", self.exploration_order, "\n")


if __name__ == "__main__":
    my_graph = graph()
    my_vtx = vertex('A')
    my_graph.add_vertex(my_vtx)

    for i in range(ord('A'), ord('V')):
        my_graph.add_vertex(vertex(chr(i)))
    
    # edges = ['AB', 'AC', 'BD', 'BE','CF','CG','CH']
    edges = ['AB', 'AC', 'AD', 'BE','BF','CG','CH','DI','DJ',
            'EK','EL','FL','FM','GN','HO','HP','IP','IQ','JR',
            'KS','LT','PU']

    for edge in edges:
        my_graph.add_edge(edge[:1],edge[1:])
    
    my_graph.print_graph()
    my_graph.bfs(my_vtx)
    my_graph.print_graph_bfs()