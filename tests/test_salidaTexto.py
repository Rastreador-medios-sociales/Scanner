import pytest
from src import salidaTexto

PROJECTNAME = "Scanner"
ISSUEID = 2

def test_exportaPDF():
    obj1 = salidaTexto.PEDEFE()
    assert salidaTexto.PEDEFE.exportaPDF(obj1, "test.pdf", "Probando el modulo de pdf") == "test.pdf"