import pytest
from src import abstractBD

PROJECTNAME = "Scanner"
ISSUEID = 3

def test_initialiceBD():
    obj1 = abstractBD.BaseDatos()
    assert abstractBD.BaseDatos.initialiceBD(obj1) == 555

def test_getDataBD():
    obj1 = abstractBD.BaseDatos()
    assert abstractBD.BaseDatos.getData(obj1) == 556

def test_setData():
    obj1 = abstractBD.BaseDatos()
    assert abstractBD.BaseDatos.setData(obj1) == 557