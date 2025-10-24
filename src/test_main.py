# test_main.py
import matplotlib.pyplot as plt
import pytest
import pytest
import numpy as np
from main import calcular_simulacao  # Substitua por uma função do main.py

def test_calcular_simulacao():
    resultado = calcular_simulacao(0)  # Ajuste o input
    assert np.allclose(resultado, 0.0, atol=1e-5)  # Ajuste o valor esperado

@pytest.mark.mpl_image_compare
def test_grafico():
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])  # Substitua pela sua lógica
    return fig
    
