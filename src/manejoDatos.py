class ManejadorDatos:
    

    def __init__(self,ruta):
        self.lugares = []
        
        

    def extraerDatos(self,ruta):
 
        archivo = open(ruta,'r')
        linea = archivo.readline()
        lugares.append(linea)
        print lugares
    


    def guardarDatos(self):
        pass

    def ordenarResultados(self):
        pass


ruta = '/home/angela/Escritorio/places.txt'
#f = open(ruta, 'r')
#
#print (f.read())

obj1 = ManejadorDatos(ruta) 
ManejadorDatos.extraerDatos(obj1,ruta)
