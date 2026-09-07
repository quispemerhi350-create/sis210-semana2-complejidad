"""
Desafio avanzado: punto de equilibrio para decidir si conviene ordenar
antes de hacer busquedas repetidas (seccion 16 del PDF).
Usa los tiempos reales obtenidos en benchmark.py para n=100,000,
escenario "ausente" (peor caso).
"""

# Tiempo de ordenar el arreglo una vez (de tiempos_ordenamiento.csv, n=100000)
prep = 1680260

# Tiempo promedio de UNA busqueda, sin ordenar (lineal) y con arreglo ya
# ordenado (binaria), de resumen_estadistico.csv, n=100000, escenario ausente
costo_lineal = 20811188.20
costo_binaria = 4194507.20

# Punto de equilibrio: numero de consultas (q) a partir del cual
# ordenar + buscar binaria sale mas barato que buscar lineal repetidamente
q_equilibrio = prep / (costo_lineal - costo_binaria)

print(f"Tiempo de preparacion (ordenar, n=100000): {prep} ns")
print(f"Costo por consulta - lineal (sin ordenar):  {costo_lineal} ns")
print(f"Costo por consulta - binaria (ya ordenado):  {costo_binaria} ns")
print(f"\nPunto de equilibrio: q = {q_equilibrio:.4f} consultas")
print("\nInterpretacion: a partir de este numero de consultas, ordenar una vez")
print("y usar busqueda binaria repetidamente sale mas barato en total que")
print("usar busqueda lineal sin ordenar en cada consulta.")
