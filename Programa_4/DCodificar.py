class programa04():

    def __init__(self,string):
        self.string = string
        self.quitar_str = ""
        
    def limpiar(self):
        self.limpiar_str = self.string.upper().replace(" ","")
          
    def encode(self, clave):
        self.limpiar()
        clave = int(clave)
        tabla = []
        #Traslacion de la cadena a la tabla
        while len(self.limpiar_str) > 0:
            aux=[]
            for i in range(0,clave):
                if len(self.limpiar_str) > 0:
                    aux.append(self.limpiar_str[0])
                    self.limpiar_str = self.limpiar_str[1:]
                else:
                    aux.append("S")
            tabla.append(aux)
        
        filas = len(tabla)
        columnas = len(tabla[0])
        auxStr = ""
        for i in range (0,columnas):
            for j in range(0,filas):
                auxStr += tabla [j][i]
        return auxStr

    def decode(self, clave)