from main import os10MaioresEstadosDoBrasil


def test_10MaioresEstadosDoBrasil():
    estados = os10MaioresEstadosDoBrasil()
    assert estados
    assert len(estados) == 10
