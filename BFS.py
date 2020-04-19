arbol = {'A':['B','C'],
        'B':['D','E'],
        'C':['F'],
        'D':[],
        'E':['F'],
        'F':[]}

class progBusqueda():

    def __init__(self):
        self.Agenda=[]
        self.Expandidos=[]

    def bfs(self):
        inicio = 'A'
        self.Expandidos.append(inicio)
        self.Agenda.append(inicio)
        print(self.Agenda)
        print(self.Expandidos)
        while self.Agenda:
            elemento = self.Agenda.pop(0) #Sacamos elemento del tope
            print(elemento, end = " ")

            for siguiente in arbol[elemento]:
                if siguiente not in self.Expandidos:
                    self.Expandidos.append(siguiente)
                    self.Agenda.append(siguiente)


busqueda = progBusqueda()
busqueda.bfs()

