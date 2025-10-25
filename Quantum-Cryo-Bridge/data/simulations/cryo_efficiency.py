import numpy as np
import os

def run_cryo_efficiency(output_dir="data/sample_run_2024"):
    """Calcula a eficiência de um sistema criogênico em diferentes potências."""

    print("🔋 Calculando eficiência criogênica...")
    power_input = np.linspace(10, 100, 10)
    efficiency = 0.8 * np.exp(-0.01 * power_input)

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "cryo_efficiency_results.csv")

    np.savetxt(output_file, np.column_stack((power_input, efficiency)), delimiter=",", header="potencia(W),eficiencia", comments="")
    print(f"✅ Resultados salvos em: {output_file}\n")
