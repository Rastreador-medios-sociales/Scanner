import pytest
from src import manejoDatos

PROJECTNAME = "Scanner"
ISSUEID = 1

def test_extraerDatos():
    obj1 = manejoDatos.ManejadorDatos("test.txt")
    assert manejoDatos.ManejadorDatos.extraerDatos(obj1, "test.txt") == ['Prueba de Texto1\n', 'Prueba de Texto2\n']

def test_guardarDatos():
    obj1 = manejoDatos.ManejadorDatos("test.txt")
    assert manejoDatos.ManejadorDatos.guardarDatos(obj1, "test") == "test"