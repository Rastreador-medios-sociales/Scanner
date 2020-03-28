import abc

class BaseDatos():
    @abc.abstractmethod
    #Este la usaremos para conectar/crear la BBDD
    def initialiceBD(self): 
        print("Soy el metodo inicializador de Bases de Datos de la clase abstracta")
        return 555
        
    @abc.abstractmethod
    #Este para rescatar un dato de la BBDD
    def getData(self):
        print("Soy el metodo de consulta de Bases de Datos de la clase abstracta")
        return 556

    @abc.abstractmethod
    #Este para guardar algo en la BBDD
    def setData(self):
        print("Soy el metodo almacenador de Bases de Datos de la clase abstracta")
        return 557