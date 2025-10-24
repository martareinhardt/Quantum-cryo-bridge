# ==============================================================================
# Caminhos de Ficheiros Padrão
# ==============================================================================
DEFAULT_DATASET = 'sample_run_2024'  # Nome de uma sub-pasta padrão em 'data/'
REPORT_OUTPUT_DIR = 'reports/'      # Onde os relatórios e gráficos serão salvos

# ==============================================================================
# Parâmetros de Medição Criogénica
# ==============================================================================
# Temperatura de operação do chip quântico (supercondutor) em Kelvin (K)
QUBIT_TEMPERATURE_K = 0.015  # 15 mK (millikelvins) é comum para qubits supercondutores

# Temperatura de uma etapa intermédia da "ponte" criogénica (em K)
BRIDGE_STAGE_TEMPERATURE_K = 3.0   # 3 K é um estágio comum para eletrónica Cryo-CMOS

# Frequência de ressonância ou operação esperada em GHz
RESONANCE_FREQUENCY_GHZ = 5.0      # Faixa de micro-ondas típica

# Potência do sinal de controlo em dBm (decibéis em relação a 1 milliwatt)
CONTROL_POWER_DBM = -100.0         # Níveis muito baixos são comuns

# ==============================================================================
# Parâmetros do Modelo de Simulação
# ==============================================================================
# Parâmetros para o modelo que simula a perda de coerência (T1, T2)
MODEL_PARAMS = {
    'qubit_type': 'transmon',  # Tipo de qubit
    'thermal_noise_factor': 0.1, # Fator de ruído devido à ponte
    'material_loss_rate': 1e-6   # Taxa de perda do material (ex: perdas dielétricas)
}
