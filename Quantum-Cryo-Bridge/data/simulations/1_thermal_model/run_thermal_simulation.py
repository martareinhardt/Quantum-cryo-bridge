import pandas as pd
import json
import numpy as np

# Função para estimar a carga térmica no estágio de 4K (Steady-State)
def calculate_4K_heat_load():
    
    print("--- Starting 4K Steady-State Heat Load Calculation ---")
    
    # 1. READ INPUT DATA
    # O script assumiria que 'input_material_properties.csv' e 'thermal_geometry_spec.json' 
    # já estão no caminho correto.
    try:
        # Lendo o CSV de materiais (substitua o caminho conforme necessário no seu ambiente)
        material_data = pd.read_csv('../../data/input_material_properties.csv')
        
        # Lendo as especificações geométricas
        with open('thermal_geometry_spec.json', 'r') as f:
            geometry = json.load(f)
            
    except FileNotFoundError as e:
        print(f"ERROR: Could not find input file: {e}")
        return

    # 2. EXTRACT KEY PARAMETERS
    
    # Parâmetros de Temperatura
    T_77K = geometry['Boundary_Conditions']['Cryocooler_Interface_77K'] # 77.0 K
    T_4K = geometry['Boundary_Conditions']['Cryocooler_Interface_4K']   # 4.2 K
    
    # Parâmetros Geométricos dos Suportes 77K -> 4K
    support_spec = geometry['Support_Structure_Parameters']
    N_rods = support_spec['Number_of_Rods']
    L_rod_m = support_spec['Rod_Length_mm'] / 1000.0  # Convert to meters
    D_rod_m = support_spec['Rod_Diameter_mm'] / 1000.0  # Convert to meters
    A_rod = np.pi * (D_rod_m / 2.0)**2  # Area of one rod
    
    # Material (Usando G-10 como exemplo para o intervalo 77K -> 4K)
    support_material = 'G-10_Fiberglass'
    # Simplificação: Em um modelo real, a condutividade k(T) seria integrada (integral) 
    # sobre o intervalo de temperatura T_77K a T_4K. 
    # Aqui, usaremos um valor médio ou o valor de 4.2K como estimativa inicial.
    k_4K = material_data[
        (material_data['Material_ID'] == support_material) & 
        (material_data['T_K'] == T_4K)
    ]['Thermal_Conductivity_W_mK'].iloc[0] # ~0.02 W/(m·K)
    
    
    # 3. CONDUCTION CALCULATION (77K -> 4K)
    # Fórmula de Condução Simples: Q = (N * k * A / L) * dT
    # Note: Esta é uma grande simplificação. Na realidade k não é constante.
    
    Q_conduction_W = N_rods * (k_4K * A_rod / L_rod_m) * (T_77K - T_4K)
    
    print(f"\n--- Conduction Heat Load ---")
    print(f"  Material (Simplificado): {support_material}")
    print(f"  Single Rod Area (A): {A_rod*1e6:.2f} mm²")
    print(f"  Temperature Difference (dT): {T_77K - T_4K:.1f} K")
    print(f"  Total Conduction Load (Q_cond): {Q_conduction_W * 1000:.4f} mW")
    
    # 4. RADIATION CALCULATION (77K Shield to 4K Shield)
    # Q_rad = sigma * A_eff * F_rad * (T_quente^4 - T_frio^4)
    # A_eff: área efetiva; F_rad: fator de forma e emissividade.
    
    # Usaremos uma simplificação apenas com emissividade e áreas estimadas
    sigma = 5.670374419e-8 # Stefan-Boltzmann constant (W/(m^2·K^4))
    
    # Pega Emissividade da Blindagem 77K (Alumínio)
    e_77K = material_data[
        (material_data['Material_ID'] == 'Aluminum_6061_T6') & 
        (material_data['T_K'] == T_77K)
    ]['Emissivity_ratio'].iloc[0] # ~0.05
    
    # Pega Emissividade da Blindagem 4K (Cobre)
    e_4K = material_data[
        (material_data['Material_ID'] == 'Copper_OFHC_Polished') & 
        (material_data['T_K'] == T_4K)
    ]['Emissivity_ratio'].iloc[0] # ~0.02
    
    # Fator de Emissividade Efetiva (assumindo F=1 e duas placas paralelas/concêntricas)
    e_eff = 1.0 / ( (1.0/e_77K) + (1.0/e_4K) - 1.0 ) # ~0.019
    
    # Área de Radiação (Área lateral da blindagem 4K, ~50cm de diâmetro, 50cm de altura)
    A_rad_m2 = np.pi * (geometry['Geometric_Parameters_Shields'][1]['Height_mm']/1000.0) * (geometry['Geometric_Parameters_Shields'][1]['Thickness_mm']/1000.0) # Simplificação da área, 0.5m * 0.005m
    A_rad_m2 = 0.8  # Aproximação de 0.8 m² para um cilindro interno típico
    
    Q_radiation_W = sigma * A_rad_m2 * e_eff * (T_77K**4 - T_4K**4)
    
    print(f"--- Radiation Heat Load ---")
    print(f"  Emissivity Effective (e_eff): {e_eff:.4f}")
    print(f"  Radiation Area (A_rad): {A_rad_m2:.2f} m²")
    print(f"  Total Radiation Load (Q_rad): {Q_radiation_W * 1000:.4f} mW")
    
    # 5. TOTAL ESTIMATE
    Q_total_4K_mW = (Q_conduction_W + Q_radiation_W) * 1000
    
    print("\n==============================================")
    print(f"  TOTAL ESTIMATED HEAT LOAD on 4K Stage: {Q_total_4K_mW:.4f} mW")
    print("==============================================")
    
# Chame a função para rodar o teste
# execute
# calculate_4K_heat_load()
 
