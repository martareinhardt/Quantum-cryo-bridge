"""
data_transmission.py — Simulação da transmissão de dados quânticos e análise de crosstalk.
"""

import random

def analisar_crosstalk():
    """
    Analisa interferência (crosstalk) entre canais quânticos simulados.
    Retorna estatísticas de ruído e taxa de erro.
    """
    print("📡 Analisando interferência de dados quânticos (crosstalk)...")

    canais = 5
    resultados = []
    for canal in range(1, canais + 1):
        ruido = random.uniform(0.001, 0.05)
        erro = random.uniform(0.0, 0.1)
        resultados.append({"canal": canal, "ruido": ruido, "taxa_erro": erro})

    print("✅ Análise de crosstalk concluída.")
    return {"status": "ok", "resultados": resultados}
