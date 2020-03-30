import pytest 
from src import inyectoraBD


PROJECTNAME = "Scanner"
ISSUEID = 4

def test_initialiceBD():
    obj1 = inyectoraBD.Inyectora()
    assert inyectoraBD.Inyectora.initialiceBD(obj1) == 558

def test_setData():
    nuevo = ('migueorg', 'Migue', 'migueorg@correo.ugr.es')
    obj1 = inyectoraBD.Inyectora()
    assert inyectoraBD.Inyectora.setData(obj1,nuevo) == 559

def test_getDataBD():
    obj1 = inyectoraBD.Inyectora()
    assert inyectoraBD.Inyectora.getData(obj1) == 560
