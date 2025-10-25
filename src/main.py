"""
main.py — módulo principal do Quantum Cryo Bridge
Executa as simulações quânticas, criogênicas e de transmissão de dados.
"""

import os
import sys
from datetime import datetime

# Caminho base do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data", "sample_run_2024")

def verificar_pasta_dados():
    """
    Verifica se a pasta de dados existe.
    Se não existir, exibe erro e interrompe a execução.
    """
    print(f"📂 Diretório base: {BASE_DIR}")
    print(f"📊 Pasta de dados: {DATA_DIR}")

    if not os.path.exists(DATA_DIR):
        raise FileNotFoundError(
            f"ERRO: Pasta de dados não encontrada em: {DATA_DIR}\n"
            "Dica: Crie 'data/sample_run_2024' com os arquivos necessários."
        )

def rodar_simulacoes():
    """
    Executa todas as simulações principais da ponte quântica criogênica.
    """
    print("\n🚀 Iniciando simulações quânticas...")

    try:
        from simulations.quantum_bridge import executar_ponte_quantica
        from simulations.cryo_dynamics import simular_dinamica_criogenica
        from simulations.data_transmission import analisar_crosstalk
    except ModuleNotFoundError as e:
        print(f"❌ Erro ao importar módulos: {e}")
        print("💡 Verifique se a pasta 'src/simulations' contém __init__.py e os arquivos .py.")
        sys.exit(1)

    resultados_ponte = executar_ponte_quantica()
    resultados_cryo = simular_dinamica_criogenica()
    resultados_crosstalk = analisar_crosstalk()

    print("\n✅ Simulações concluídas com sucesso!")
    print(f"🔗 Ponte quântica: {resultados_ponte}")
    print(f"🧊 Dinâmica criogênica: {resultados_cryo}")
    print(f"📡 Transmissão de dados: {resultados_crosstalk}")

def salvar_log_execucao():
    """
    Salva um log da execução no diretório 'logs'.
    """
    logs_dir = os.path.join(BASE_DIR, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    log_path = os.path.join(
        logs_dir, f"execucao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    with open(log_path, "w", encoding="utf-8") as f:
        f.write("Execução concluída com sucesso.\n")
        f.write(f"Data: {datetime.now()}\n")
        f.write(f"Diretório de dados: {DATA_DIR}\n")

    print(f"📝 Log salvo em: {log_path}")

def main():
    try:
        verificar_pasta_dados()
        rodar_simulacoes()
        salvar_log_execucao()
    except Exception as e:
        print(f"❌ Erro fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
