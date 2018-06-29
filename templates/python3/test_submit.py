from main import os10MaioresEstadosDoBrasil


def test_Submit10MaioresEstadosDoBrasil():
    estados = os10MaioresEstadosDoBrasil()
    assert estados
    assert len(estados) == 10
    expected =["Amazonas", "Pará", "Mato Grosso", "Minas Gerais", "Bahia",
               "Mato Grosso do Sul", "Goiás", "Maranhão", "Rio Grande do Sul", "Tocantins"]
    assert estados == expected
