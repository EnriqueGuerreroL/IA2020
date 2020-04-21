# Alumnos:
# FUENTES MORA OSCAR FERNANDO 	
# GRANADOS GÓMEZ NANCI NOELIA 
# GUERRERO LÓPEZ ENRIQUE
# PÓLITO SEBA VÍCTOR HUGO

class vertex:
    """Clase vertex con la que representaremos un vértice.

    Con esta clase entregaremos un objeto (vertex) con varias propiedades útiles para
    nuestra implementación de los algoritmos.
    
    Recibe como parámetro el nombre del vértice.

    Contiene un método para agregar vértices un vértice adyacente.

    """
    def __init__(self, n):
        self.name = n
        self.adjacent_vertices = []
        self.color = 'white'
        self.predecessor = -1
        # para BFS
        self.distance = 9999 
        # para DFS
        self.discovery_time = 0
        self.finishing_time = 0

    def add_adjacent_vertex(self, vertex):
        """Método para añadir un vértice adyacente.

        Si el supuesto nuevo vértice no existe en la lista de vértices
        adyacentes, se agrega como adyacente.

        Recibe como parámetro el nombre del vértice vecino.     

        """
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            self.adjacent_vertices.sort()


class graph:
    """Clase para representar una gráfica, en este caso dirigida.

    Esta clase implementa varios métodos, unos para definir la estructura
    de la gráfica y otros para la búsqueda en la misma.

    Parámetros:
    No recibe parámetros para hacer una instancia de la clase.

    """
    vertices = {}
    exploration_order = []
    time = 0

    def add_vertex(self, a_vertex):
        """Con este método se agrega un vértice a la gráfica.

        Si recibe una instancia de la clase vertex y aún no existe en la gráfica, 
        agrega el vértice recibido.

        Parámetros:
        Objeto de la clase vertex (vértice).
        
        """
        if isinstance(a_vertex, vertex) and a_vertex.name not in self.vertices:
            self.vertices[a_vertex.name] = a_vertex
            return True
        else:
            return False
        
    def add_edge(self, a_vertex, another_vertex):
        """Método para agregar una arista a la gráfica.

        Si los dos vértices que recibe existen en la gráfica, forma la relación
        entre los vértices, siendo el primero el padre y el segundo el hijo.

        Parámetros:
        Nodo padre
        Nodo hijo

        """
        if a_vertex in self.vertices and another_vertex in self.vertices:
            for key, value in self.vertices.items():
                if key == a_vertex:
                    value.add_adjacent_vertex(another_vertex)
            return True
        else:
            return False

    def print_graph(self):
        """Método para imprimir la gráfica como una lista de adyacencia tal y como fue definida.
        
        No recibe parámetros.
        
        """
        print("\n\tGrafica:")
        for key in sorted(list(self.vertices.keys())):
            print("Vertice " + key + ": " + str(self.vertices[key].adjacent_vertices))
    
    def print_graph_bfs(self):
        """Método para imprimir los datos generados tras la ejecución del algoritmo BFS.
        
        No recibe parámetros.
        
        """
        print("\n\tBFS:")
        for key in sorted(list(self.vertices.keys())):
            print("La distancia de A a " + key + " es: " + str(self.vertices[key].distance))
        print("\nRecorrido de la grafica: ", self.exploration_order,"\n")

    def print_graph_dfs(self):
        """Método para imprimir los datos generados tras la ejecución del algoritmo DFS.

        No recibe parámetros.
        
        """
        print("\n\tDFS:")
        for key in sorted(list(self.vertices.keys())):
            print("Vertice: " + key)
            print("\tDescubierto/Termino: " + str(self.vertices[key].discovery_time) + "/" + str(self.vertices[key].finishing_time))
        print("\nRecorrido de la grafica: ", self.exploration_order,"\n")

    def bfs(self, a_vertex):
        """Método para ejecutar el BFS sobre la gráfica.

        Para este algoritmo, se va a explorar cada nodo y hasta que todos los nodos adyacentes
        estén descubiertos (color gris) podremos decir que se ha explorado por completo 
        el vértice (color negro). 
        Para el control del orden en que se van a explorar los nodos conforme se van descubriendo,
        utilizamos una cola FIFO.
        Cada vez que se descubre un vértice, se colorea de gris, se le asigna la distancia del nodo que se está
        explorando hasta ese vertice vecino y se le asigna el vértice predecesor. El vértice recién descubierto
        se agrega a la cola para después explorar sus vecinos.
        Termina cuando todos los vértices están en color negro.

        Parámetros:
        Vértice de origen, con el que se comenzará el algoritmo. 
        
        """
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
    
    def dfs(self, vertex):
        """Método para ejecutar el DFS sobre la gráfica.

        Para cada uno de los vértices de la gráfica que esté como no descubierto (color blanco),
        se mandará a visitar mediante el método dfs_visit.

        Parámetros:
        Vértice de origen, con el que se comenzará el algoritmo.

        """
        global time
        time = 0
        for vrtx in sorted(list(self.vertices.keys())):
            if self.vertices[vrtx].color == 'white':
                self.dfs_visit(self.vertices[vrtx])
    
    def dfs_visit(self, vertex):
        """Método recursivo que realiza la exploración del vértice que recibe.

        Modifica al vértice que recibe en sus atributos tiempo de descubrimiento y color,
        posteriormente, revisa en cada uno de los vértices adyacentes si hay elementos
        no descubiertos; si ese es el caso, descubre ese vértice e inmediatamente lo manda
        a explorar; así, logra llegar hasta el nodo más profundo en la gráfica.
        Una vez que se finaliza la exploración del vértice, se le asigna el tiempo en el que 
        termina de ser explorado.

        Parámetros:
        Vértice a explorar.

        """
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
    """Entrada del programa.

    Se realiza la instancia de la gráfica que se va a trabajar, del vértice de inicio y 
    del resto de vértices que commponen la gráfica. Se está utilizando el abecedario para
    nombrar los vértices de la gráfica. Para definir los vértices de la gráfica se utilizan
    cadenas de dos caracteres.
    Nota: se debe utilizar un algoritmo por gráfica o comentar el algoritmo que no se 
    quiere probar.
    Desde esta función se manda a llamar a los métodos de la gráfica a trabajar.
    """
    my_graph = graph()
    source_vrtx = vertex('A')
    my_graph.add_vertex(source_vrtx)

    for i in range(ord('A'), ord('V')):
        my_graph.add_vertex(vertex(chr(i)))
    
    edges = ['AB', 'AC', 'AD', 'BE','BF','CG','CH','DI','DJ',
            'EK','EL','FL','FM','GN','HO','HP','IP','IQ','JR',
            'KS','LT','PU']

    for edge in edges:
        my_graph.add_edge(edge[:1],edge[1:])
    
    # muestra en consola la gráfica como lista de adyacencia
    my_graph.print_graph()

    # par de líneas para BFS
    my_graph.bfs(source_vrtx)
    my_graph.print_graph_bfs()

    # par de líneas para DFS
    # my_graph.dfs(source_vrtx)
    # my_graph.print_graph_dfs()