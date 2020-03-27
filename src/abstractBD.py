import abc

class BaseDatos(abc.ABC):
    @abc.abstractmethod
    #Este la usaremos para conectar/crear la BBDD
    def initialiceBD(self): 
        pass

    @abc.abstractmethod
    #Este para rescatar un dato de la BBDD
    def getData(self):
        pass

    @abc.abstractmethod
    #Este para guardar algo en la BBDD
    def setData(self):
        pass