import os 
dir = os.path.dirname(__file__) 
dir2 = os.path.dirname(__file__) 
dir3 = os.path.dirname(__file__)

class ManejadorDatos:
    
    def __init__(self,ruta):
        self.lugares = []
        
        

    def extraerDatos(self,ruta):
 
        filename3 = os.path.join(dir3, ruta)
        archivo = open(filename3,'r')
        for linea in archivo:
            self.lugares.append(linea)
            #linea = archivo.readline()
        
        print (self.lugares)
        return self.lugares


    def guardarDatos(self):
        pass

    def ordenarResultados(self):
        pass




#Main improvisado para hacer pruebas

filename = os.path.join(dir, 'places.txt')

filename2 = os.path.join(dir2, 'test.txt')

#ruta = 'places.txt'
f = open(filename, 'r')

#print (f.read())

obj1 = ManejadorDatos(filename) 
ManejadorDatos.extraerDatos(obj1,filename)

obj2 = ManejadorDatos(filename2)
obj2.extraerDatos(filename2)
