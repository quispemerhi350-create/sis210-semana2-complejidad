# SIS210 · Semana 2 · Complejidad — Búsqueda lineal vs. búsqueda binaria

Práctica de laboratorio del curso Algoritmos y Estructuras de Datos (SIS210),
Universidad Nacional del Altiplano - Puno. Analiza la complejidad teórica
(O, Ω, Θ) y empírica de dos algoritmos de búsqueda, implementados de forma
comparable en Python 3 y C++20, y evaluados mediante un benchmark reproducible
sobre datos reales del dataset Online Retail (UCI).

## Qué compara este proyecto
- **Búsqueda lineal**: recorre el arreglo elemento por elemento.
- **Búsqueda binaria**: divide el espacio de búsqueda a la mitad en cada paso,
  requiere que el arreglo esté ordenado.
- Clave de búsqueda: `CustomerID` (identificador de cliente) del dataset.

## Requisitos previos
Para reproducir el experimento completo necesitas:
1. **Python 3.11 o superior**, con las librerías `pandas`, `numpy` y
   `matplotlib` (instalables con `pip install pandas numpy matplotlib`).
2. **El dataset Online Retail**, que NO está incluido en este repositorio
   (pesa varios MB y es un dataset de terceros con su propia licencia).
   Debes descargarlo tú mismo:
   - Ve a: https://archive.ics.uci.edu/dataset/352/online+retail
   - Descarga el archivo comprimido y extráelo.
   - Dentro encontrarás `Online Retail.xlsx` — cópialo a la misma carpeta
     donde vayas a ejecutar `benchmark.py`.
   - Licencia del dataset: CC BY 4.0. DOI: https://doi.org/10.24432/C5BW33
3. (Opcional, solo si quieres recompilar C++) un compilador compatible con
   C++20, como g++.

Sin el archivo `Online Retail.xlsx` en la misma carpeta, `benchmark.py`
arrojará un error `FileNotFoundError` al intentar leerlo — esto es esperado
y se soluciona colocando el archivo ahí antes de ejecutar.

## Versiones utilizadas durante el desarrollo
- Python 3.14.2
- pandas, matplotlib, numpy (última versión disponible vía pip a la fecha)
- g++ 16.1.0 (MinGW-w64) — usado únicamente para el código base de C++ en la
  Fase A (línea base). El benchmark completo con datos reales se ejecutó en
  Google Colab (entorno Linux), debido a un error de "undefined reference to
  WinMain" detectado en la instalación local de g++ en Windows; el problema
  y su solución están documentados en el informe técnico.
- git 2.55.0

## Estructura del repositorio y qué hace cada archivo
| Archivo | Fase del PDF | Contenido |
|---|---|---|
| `busqueda.py` / `busqueda.cpp` | A: Línea base | Funciones de búsqueda lineal y binaria con conteo de comparaciones |
| `analisis-teorico.md` | B: Analizar | Derivación de T(n), O, Ω, Θ y casos para ambos algoritmos |
| `instrumentacion.py` | C: Instrumentar | Generación de los 4 escenarios (inicio/centro/final/ausente) y funciones de medición |
| `benchmark.py` | D-E: Experimentar y Visualizar | Script completo: carga el dataset, arma las muestras, corre 30 repeticiones por combinación, calcula estadísticas y genera los gráficos |
| `resultados_busqueda.csv` | D | Datos crudos del benchmark (960 filas: 4 n × 4 escenarios × 30 repeticiones × 2 algoritmos) |
| `tiempos_ordenamiento.csv` | D | Tiempo de ordenamiento por cada n (medido por separado del tiempo de búsqueda) |
| `resumen_estadistico.csv` | E | Promedio, mediana, mínimo y máximo por combinación (32 filas) |
| `grafico_n_vs_comparaciones.png`, `grafico_n_vs_tiempo.png` | E | Gráficos exigidos por la práctica |
| `informe-tecnico.md` (o .docx) | Informe | Documento completo: marco teórico, método, resultados, discusión y conclusiones |
| `declaracion-ia.md` | Declaración de IA | Uso de IA durante el desarrollo |

## Cómo reproducir el experimento paso a paso
1. Clona o descarga este repositorio.
2. Descarga `Online Retail.xlsx` siguiendo las instrucciones de "Requisitos
   previos" y colócalo en la misma carpeta que `benchmark.py`.
3. Instala las dependencias (si no las tienes):
