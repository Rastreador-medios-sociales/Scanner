import abstractBD
import sqlite3


class Inyectora(abstractBD.BaseDatos):

     def __init__(self):
        self.conector = sqlite3.connect('baseDatos.db')
        self.miBD = self.conector.cursor()


     def initialiceBD(self):

        print("Creo BD")  

        self.miBD.execute("CREATE TABLE usuarios(id integer PRIMARY KEY, nick text, name text, email text)")

        self.conector.commit()


     def setData(self):
        print("Almaceno en BD")

        self.miBD.execute("INSERT INTO usuarios VALUES(1, 'agr8','Angy', 'angelagr@correo.ugr.es')")
        
        nueva = (2, 'migueorg','Migue', 'migueorg@correo.ugr.es')

        self.miBD.execute('''INSERT INTO usuarios(id, nick, name, email) VALUES(?, ?, ?, ?)''', nueva)

        self.conector.commit()     

     def getData(self):
        print("Obtengo de BD")

        self.miBD.execute('SELECT * FROM usuarios')

        rows = self.miBD.fetchall()
        
        for row in rows:

            print(row)
        

  


        

obj1 = Inyectora()


obj1.initialiceBD()
obj1.setData()
obj1.getData()


