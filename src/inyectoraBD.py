import abstractBD
import sqlite3

class Inyectora(abstractBD.BaseDatos):
    def initialiceBD(self):
        print("Creo BD")  

    def getData(self):
        print("Obtengo de BD")

    def setData(self):
        print("Almaceno en BD")

#abstractBD.BaseDatos.register(Inyectora)
obj1 = Inyectora()

obj1.initialiceBD()
obj1.getData()
obj1.setData()