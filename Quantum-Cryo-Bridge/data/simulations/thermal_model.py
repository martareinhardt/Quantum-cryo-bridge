import numpy as np
import matplotlib.pyplot as plt
import os

def run_thermal_simulation(output_dir="data/sample_run_2024"):
    """Simula o resfriamento exponencial de um sistema criogênico."""

    print("🧊 Rodando simulação térmica...")
    time = np.linspace(0, 10, 100)
    temperature = 300 * np.exp(-0.4 * time)

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "thermal_model_results.csv")

    np.savetxt(output_file, np.column_stack((time, temperature)), delimiter=",", header="tempo,temperatura(K)", comments="")
    print(f"✅ Resultados salvos em: {output_file}")

    plt.plot(time, temperature, label="Temperatura (K)")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Temperatura (K)")
    plt.title("Resfriamento do sistema criogênico")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "thermal_plot.png"))
    plt.close()
    print("📊 Gráfico térmico gerado!\n")
