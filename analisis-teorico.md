# Análisis teórico — Búsqueda lineal vs. búsqueda binaria

## 1. Tamaño de entrada n
n = número de elementos del arreglo/lista donde se realiza la búsqueda (len(datos)).

## 2. Operación dominante
La comparación entre el valor buscado y un elemento del arreglo:
- Lineal: `if valor == x`
- Binaria: `if a[medio] == x`
Es la operación que se cuenta en la variable `ops` del código base, y la que determina el costo real de cada algoritmo.

## 3. Función de costo T(n)

### Búsqueda lineal
- Peor caso (valor al final o ausente): T(n) = n
- Mejor caso (valor en la posición 0): T(n) = 1
- Caso promedio (valor en cualquier posición con igual probabilidad): T(n) ≈ n/2

### Búsqueda binaria
- Peor caso (valor ausente o en un extremo): T(n) ≈ ⌈log₂(n)⌉ + 1
- Mejor caso (valor justo en la posición medio de la primera iteración): T(n) = 1
- Caso promedio: T(n) ≈ log₂(n)

Justificación del logaritmo en binaria: cada iteración descarta la mitad del espacio de búsqueda restante. Partiendo de n elementos, tras k iteraciones quedan n/2^k elementos. El proceso termina cuando n/2^k = 1, es decir, k = log₂(n).

## 4. Notación asintótica (O, Ω, Θ)

O(g(n)): cota superior. T(n) ∈ O(g(n)) si existen c > 0 y n₀ tales que T(n) ≤ c·g(n) para todo n ≥ n₀.
Ω(g(n)): cota inferior. T(n) ∈ Ω(g(n)) si existen c > 0 y n₀ tales que T(n) ≥ c·g(n) para todo n ≥ n₀.
Θ(g(n)): cota ajustada, cuando T(n) está en O(g(n)) y en Ω(g(n)) al mismo tiempo.

Importante: O, Ω y Θ describen la forma de crecimiento de T(n), no un escenario de entrada. "Mejor caso" y "peor caso" describen qué tipo de entrada recibe el algoritmo. Son dos ejes independientes que se combinan (ej. "el peor caso de la lineal es Θ(n)"), pero no son sinónimos entre sí.

| Algoritmo | Mejor caso | Peor caso | Caso promedio |
|---|---|---|---|
| Lineal | Θ(1) | Θ(n) | Θ(n) |
| Binaria | Θ(1) | Θ(log n) | Θ(log n) |

## 5. Por qué Ω no es sinónimo automático de "mejor caso"
En el peor caso de la búsqueda lineal, T(n) = n. Ese mismo peor caso tiene una cota superior O(n) y también una cota inferior Ω(n) (en el peor caso, el algoritmo nunca hace menos de n comparaciones). Es decir, Ω también describe el peor caso, no solo el mejor. Ω únicamente expresa "esto no puede crecer más lento que...", sin importar de qué caso se trate.

## 6. Predicción teórica para el experimento
- Búsqueda lineal: crecimiento lineal de comparaciones y tiempo respecto a n.
- Búsqueda binaria: crecimiento logarítmico de comparaciones y tiempo respecto a n.