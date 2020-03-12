class ManejadorDatos:

    lugares = []

    def __init__(self):
        pass

    def extraerDatos(self,'places.txt'):
        archivo = open("places.txt")
        linea = archivo.readline()
        lugares.append(linea)
        print lugares
    


    def guardarDatos(self):
        pass

    def ordenarResultados(self):
        pass

