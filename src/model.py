# Importa bibliotecas necessárias para cálculo científico
import numpy as np
from scipy.optimize import curve_fit # Útil para ajustar modelos aos dados

# Importa as configurações do seu sistema
from . import config 

# ==============================================================================
# 1. FUNÇÕES DE AJUSTE DE MODELO (FITTING)
# ==============================================================================

def lorentzian_model(f, f0, Q, A):
    """
    Modelo de ressonador de micro-ondas (Lorentziana) para ajuste de dados S21.
    
    f: Frequência (variável independente)
    f0: Frequência de ressonância central (parâmetro)
    Q: Fator de qualidade do ressonador (parâmetro)
    A: Amplitude de fundo (parâmetro)
    """
    # Esta é uma forma simplificada da função de ressonância (curva de amplitude)
    return A / (1 + 4 * Q**2 * ((f - f0) / f0)**2)

def fit_resonance_data(processed_data: pd.DataFrame) -> dict:
    """
    Ajusta os dados de S21 (magnitude de transmissão) a um modelo Lorentzian.
    """
    print("Iniciando ajuste do modelo de ressonância...")
    
    f_data = processed_data['frequency_GHz'].values
    s21_data = processed_data['s21_smoothed'].values
    
    # ------------------- Lógica de Ajuste -------------------
    # Valores iniciais para f0, Q, A (aproximações cruciais para o fit)
    p0 = [
        config.RESONANCE_FREQUENCY_GHZ, # f0: Começa pela frequência configurada
        10000,                          # Q: Valor inicial típico de Q
        np.max(s21_data) * 0.5          # A: Começa pela metade da amplitude máxima
    ]

    try:
        # Usa scipy.optimize.curve_fit para encontrar os melhores parâmetros
        popt, pcov = curve_fit(lorentzian_model, f_data, s21_data, p0=p0)
        
        # Parâmetros otimizados
        f0_fit, Q_fit, A_fit = popt
        
        print("Ajuste do modelo concluído.")
        return {
            'fitted_frequency_GHz': f0_fit,
            'fitted_Q_factor': Q_fit,
            'fit_amplitude': A_fit
        }
    
    except RuntimeError:
        print("AVISO: O ajuste da curva não foi possível.")
        return {'error': 'Fit Failed', 'fitted_frequency_GHz': np.nan}


# ==============================================================================
# 2. FUNÇÃO DE SIMULAÇÃO (DECOHERENCE/PERDA)
# ==============================================================================

def run_simulation(processed_data: pd.DataFrame, model_params: dict) -> dict:
    """
    Simula o impacto da ponte criogénica na coerência do qubit (ex: tempo T1).
    
    Esta é a parte que simula a física do 'Cryo-Bridge'.
    """
    print("Iniciando simulação do impacto da ponte...")

    # Simulação baseada nos parâmetros de configuração
    T_qubit = config.QUBIT_TEMPERATURE_K
    T_bridge = config.BRIDGE_STAGE_TEMPERATURE_K
    
    # FÓRMULA DE SIMULAÇÃO (exemplo simplificado e didático)
    # A perda total (T1_loss) é inversamente proporcional à temperatura, 
    # mais a contribuição de perdas do material (material_loss_rate).
    
    # Perda térmica induzida pela ponte (simplificado)
    thermal_loss = (T_bridge / T_qubit) * 1e-8 
    
    # Tempo de coerência simulado (T1) em microsegundos (µs)
    # Quanto maior a perda, menor o T1
    total_loss_rate = thermal_loss + model_params['material_loss_rate']
    T1_simulated_us = 1.0 / total_loss_rate # Simulação inversa

    # --- Chamada à função de ajuste de modelo ---
    fit_results = fit_resonance_data(processed_data)
    
    # ---------------------------------------------
    
    results = {
        'T1_simulated_us': T1_simulated_us,
        'thermal_loss_contribution': thermal_loss
    }
    
    # Combina os resultados do ajuste e da simulação
    results.update(fit_results)
    
    return results

