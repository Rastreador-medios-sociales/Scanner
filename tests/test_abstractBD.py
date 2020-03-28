import pytest
from src import abstractBD

PROJECTNAME = "Scanner"
ISSUEID = 3

def test_itialiceBD():
    obj1 = abstractBD.BaseDatos()
    assert abstractBD.BaseDatos.initialiceBD(obj1) == 555
