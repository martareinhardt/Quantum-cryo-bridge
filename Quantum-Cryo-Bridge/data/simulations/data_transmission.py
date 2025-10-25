import numpy as np
import os

def run_data_transmission(output_dir="data/sample_run_2024"):
    """Simula a transmissão de dados sob ruído térmico."""

    print("📡 Simulando transmissão de dados...")
    distance = np.linspace(0, 100, 50)
    noise = np.random.normal(0, 0.02, len(distance))
    signal_strength = np.exp(-distance / 40) + noise

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "data_transmission_results.csv")

    np.savetxt(output_file, np.column_stack((distance, signal_strength)), delimiter=",", header="distancia(m),forca_sinal", comments="")
    print(f"✅ Resultados salvos em: {output_file}\n")
