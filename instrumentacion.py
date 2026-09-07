from time import perf_counter_ns
from busqueda import busqueda_lineal, busqueda_binaria

def generar_arreglo(n, escenario):
    """
    Genera un arreglo ORDENADO de tamano n y el valor objetivo,
    segun el escenario pedido por la practica (seccion 7.1 del PDF).
    escenario: "inicio", "centro", "final", "ausente"
    """
    arreglo = list(range(n))

    if escenario == "inicio":
        objetivo = arreglo[0]
    elif escenario == "centro":
        objetivo = arreglo[n // 2]
    elif escenario == "final":
        objetivo = arreglo[-1]
    elif escenario == "ausente":
        objetivo = n
    else:
        raise ValueError(f"Escenario no reconocido: {escenario}")

    return arreglo, objetivo


def medir_lineal(arreglo, objetivo):
    inicio = perf_counter_ns()
    pos, ops = busqueda_lineal(arreglo, objetivo)
    fin = perf_counter_ns()
    return ops, fin - inicio


def medir_binaria(arreglo, objetivo):
    inicio = perf_counter_ns()
    pos, ops = busqueda_binaria(arreglo, objetivo)
    fin = perf_counter_ns()
    return ops, fin - inicio


if __name__ == "__main__":
    for escenario in ["inicio", "centro", "final", "ausente"]:
        arreglo, objetivo = generar_arreglo(20, escenario)
        ops_l, t_l = medir_lineal(arreglo, objetivo)
        ops_b, t_b = medir_binaria(arreglo, objetivo)
        print(f"{escenario:8s} | lineal: ops={ops_l:3d} t={t_l:6d}ns | binaria: ops={ops_b:3d} t={t_b:6d}ns")
