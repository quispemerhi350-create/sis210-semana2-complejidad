"""
Benchmark: busqueda lineal vs binaria sobre CustomerID del dataset Online Retail (UCI).
Requiere: Online Retail.xlsx en el mismo directorio, y busqueda.py con las funciones base.
Genera: resultados_busqueda.csv, tiempos_ordenamiento.csv, resumen_estadistico.csv,
        grafico_n_vs_comparaciones.png, grafico_n_vs_tiempo.png
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns
from busqueda import busqueda_lineal, busqueda_binaria

REPETICIONES = 30
TAMANOS_N = [100, 1000, 10000, 100000]
ESCENARIOS = ["inicio", "centro", "final", "ausente"]
SEMILLA = 42

# --- 1. Cargar y preparar el dataset ---
df = pd.read_excel("Online Retail.xlsx")
customer_ids = df["CustomerID"].dropna().astype(int)
todos_los_ids = customer_ids.to_numpy()
print(f"Filas con CustomerID valido: {len(customer_ids)} de {len(df)} totales")

# --- 2. Generar muestras reproducibles por n ---
rng = np.random.default_rng(seed=SEMILLA)
muestras = {n: rng.choice(todos_los_ids, size=n, replace=False) for n in TAMANOS_N}

# --- 3. Correr el benchmark ---
resultados_busqueda = []
resultados_preparacion = []

for n in TAMANOS_N:
    muestra = muestras[n]

    inicio_orden = perf_counter_ns()
    arreglo_ordenado = np.sort(muestra)
    fin_orden = perf_counter_ns()
    resultados_preparacion.append({"n": n, "tiempo_ordenar_ns": fin_orden - inicio_orden})

    for escenario in ESCENARIOS:
        if escenario == "inicio":
            objetivo = int(arreglo_ordenado[0])
        elif escenario == "centro":
            objetivo = int(arreglo_ordenado[n // 2])
        elif escenario == "final":
            objetivo = int(arreglo_ordenado[-1])
        else:
            objetivo = int(arreglo_ordenado[-1]) + 1

        for rep in range(REPETICIONES):
            inicio = perf_counter_ns()
            pos_l, ops_l = busqueda_lineal(muestra.tolist(), objetivo)
            fin = perf_counter_ns()
            resultados_busqueda.append({
                "algoritmo": "lineal", "n": n, "escenario": escenario,
                "repeticion": rep, "comparaciones": ops_l, "tiempo_ns": fin - inicio
            })

            inicio = perf_counter_ns()
            pos_b, ops_b = busqueda_binaria(arreglo_ordenado.tolist(), objetivo)
            fin = perf_counter_ns()
            resultados_busqueda.append({
                "algoritmo": "binaria", "n": n, "escenario": escenario,
                "repeticion": rep, "comparaciones": ops_b, "tiempo_ns": fin - inicio
            })

    print(f"n={n:6d} completado")

df_resultados = pd.DataFrame(resultados_busqueda)
df_preparacion = pd.DataFrame(resultados_preparacion)
df_resultados.to_csv("resultados_busqueda.csv", index=False)
df_preparacion.to_csv("tiempos_ordenamiento.csv", index=False)

# --- 4. Estadisticas ---
resumen = df_resultados.groupby(["algoritmo", "n", "escenario"]).agg(
    comparaciones_promedio=("comparaciones", "mean"),
    comparaciones_mediana=("comparaciones", "median"),
    comparaciones_min=("comparaciones", "min"),
    comparaciones_max=("comparaciones", "max"),
    tiempo_ns_promedio=("tiempo_ns", "mean"),
    tiempo_ns_mediana=("tiempo_ns", "median"),
    tiempo_ns_min=("tiempo_ns", "min"),
    tiempo_ns_max=("tiempo_ns", "max"),
).reset_index()
resumen.to_csv("resumen_estadistico.csv", index=False)

# --- 5. Graficos ---
datos_grafico = resumen[resumen["escenario"] == "ausente"]

plt.figure(figsize=(8, 5))
for alg in ["lineal", "binaria"]:
    subset = datos_grafico[datos_grafico["algoritmo"] == alg]
    plt.plot(subset["n"], subset["comparaciones_promedio"], marker="o", label=alg)
plt.xlabel("n (tamaño de entrada)")
plt.ylabel("Comparaciones promedio")
plt.title("n vs. Comparaciones (escenario: ausente)")
plt.legend()
plt.grid(True)
plt.savefig("grafico_n_vs_comparaciones.png", dpi=150, bbox_inches="tight")

plt.figure(figsize=(8, 5))
for alg in ["lineal", "binaria"]:
    subset = datos_grafico[datos_grafico["algoritmo"] == alg]
    plt.plot(subset["n"], subset["tiempo_ns_promedio"], marker="o", label=alg)
plt.xlabel("n (tamaño de entrada)")
plt.ylabel("Tiempo promedio (ns)")
plt.title("n vs. Tiempo (escenario: ausente)")
plt.legend()
plt.grid(True)
plt.savefig("grafico_n_vs_tiempo.png", dpi=150, bbox_inches="tight")

print("\nBenchmark completo. Archivos generados:")
print("- resultados_busqueda.csv", df_resultados.shape)
print("- tiempos_ordenamiento.csv", df_preparacion.shape)
print("- resumen_estadistico.csv", resumen.shape)
print("- grafico_n_vs_comparaciones.png")
print("- grafico_n_vs_tiempo.png")
