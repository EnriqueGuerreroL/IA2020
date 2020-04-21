class vertex:
    def __init__(self, n):
        self.name = n
        self.adjacent_vertices = []
        self.discovery_time = 0
        self.finishing_time = 0
        self.color = 'white'
        self.predecessor = -1

    def add_adjacent_vertex(self, vertex):
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            self.adjacent_vertices.sort()


class graph:
    vertices = {}
    time = 0
    exploration_order =[]

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
                # if key == another_vertex:
                #     value.add_adjacent_vertex(a_vertex)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice: " + key)
            print("Descubierto/Termino: " + str(self.vertices[key].discovery_time) + "/" + str(self.vertices[key].finishing_time))
        print("Recorrido de la gráfica: ", self.exploration_order)

    def dfs(self, vertex):
        global time
        time = 0
        for vrtx in sorted(list(self.vertices.keys())):
            if self.vertices[vrtx].color == 'white':
                self.dfs_visit(self.vertices[vrtx])
    
    def dfs_visit(self, vertex):
        global time
        time += 1
        vertex.discovery_time = time
        vertex.color = 'gray'
        self.exploration_order.append(vertex.name)
        
        for vrtx in vertex.adjacent_vertices:
            if self.vertices[vrtx].color == 'white':
                self.vertices[vrtx].predecessor = vertex
                self.dfs_visit(self.vertices[vrtx])
        vertex.color = 'black'
        time += 1
        vertex.finishing_time = time

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
    
    # my_graph.print_graph()
    my_graph.dfs(my_vtx)
    my_graph.print_graph()