"""
main.py — módulo principal do Quantum Cryo Bridge
Executa as simulações de interface quântica com resfriamento criogênico.
"""

import os
import sys
from datetime import datetime

# === Caminhos base ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FONTE_DIR = os.path.join(BASE_DIR, "fonte")
DATA_DIR = os.path.join(BASE_DIR, "data", "sample_run_2024")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# === Garantir que o diretório de código-fonte está no PYTHONPATH ===
if FONTE_DIR not in sys.path:
    sys.path.insert(0, FONTE_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def verificar_pasta_dados():
    """
    Verifica se a pasta de dados existe.
    Se não existir, cria automaticamente (em CI) ou alerta localmente.
    """
    print(f"📂 Diretório base: {BASE_DIR}")
    print(f"📊 Pasta de dados: {DATA_DIR}")

    if not os.path.exists(DATA_DIR):
        print("⚠️ Pasta de dados não encontrada. Criando diretório vazio...")
        os.makedirs(DATA_DIR, exist_ok=True)
        print(f"📁 Criado: {DATA_DIR}")

def rodar_simulacoes():
    """
    Executa as simulações principais da ponte quântica criogênica.
    """
    print("\n🚀 Iniciando simulações quânticas...")

    try:
        from simulations.quantum_bridge import executar_ponte_quantica
        from simulations.cryo_dynamics import simular_dinamica_criogenica
    except ModuleNotFoundError as e:
        print(f"❌ Erro ao importar módulos: {e}")
        print("💡 Verifique se a pasta 'simulations' está dentro de 'fonte/' e contém __init__.py")
        raise

    resultados_ponte = executar_ponte_quantica()
    resultados_cryo = simular_dinamica_criogenica()

    print("\n✅ Simulações concluídas com sucesso!")
    print(f"🧊 Resultados criogênicos: {resultados_cryo}")
    print(f"🔗 Resultados quânticos: {resultados_ponte}")

def salvar_log_execucao():
    """
    Salva um log da execução no diretório 'logs'.
    """
    os.makedirs(LOGS_DIR, exist_ok=True)
    log_path = os.path.join(LOGS_DIR, f"execucao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

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
