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


     def setData(self, tuplas):
        print("Almaceno en BD")
        self.miBD.execute("INSERT INTO usuarios VALUES(1, 'agr8','Angy', 'angelagr@correo.ugr.es')")
        #Extrae el id que le corresponde contando las entradas de la tabla y le suma uno
        self.miBD.execute('SELECT count(*) FROM usuarios')
        numeroCols = self.miBD.fetchall()
        numer = numeroCols.pop() 
        iden = numer[0]+1 #Suma uno al número de entradas de la tabla
        iden_t = (iden,) #Pasa el int a tupla
        self.miBD.execute('''INSERT INTO usuarios(id, nick, name, email) VALUES(?, ?, ?, ?)''', iden_t+tuplas)
        self.conector.commit()     

     def getData(self):
        print("Obtengo de BD")
        self.miBD.execute('SELECT * FROM usuarios')
        rows = self.miBD.fetchall()
        
        for row in rows:
            print(row)
        

  


        

obj1 = Inyectora()

nuevo = ('migueorg', 'Migue', 'migueorg@correo.ugr.es')
obj1.initialiceBD()
obj1.setData(nuevo)
obj1.getData()


