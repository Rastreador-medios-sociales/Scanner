import os
from src import salidaTexto

from src.manejoDatos import ManejadorDatos

dir = os.path.dirname(__file__) 
dir2 = os.path.dirname(__file__) 
dir3 = os.path.dirname(__file__)


nombre = input("Dime tu nombre: ")

#nombre se le pasaría a la función getDatos, si devuelve que no existe, pues se crea con setDatos



#Main improvisado para hacer pruebas

filename = os.path.join(dir, 'src/places.txt')

filename2 = os.path.join(dir2, 'src/test.txt')

#ruta = 'places.txt'
f = open(filename, 'r')

#print (f.read())

obj1 = ManejadorDatos(filename) 
ManejadorDatos.extraerDatos(obj1,filename)

obj2 = ManejadorDatos(filename2)
obj2.extraerDatos(filename2)

obj1.guardarDatos("salidaDePrueba")