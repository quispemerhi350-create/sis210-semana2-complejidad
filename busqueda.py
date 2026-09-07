from time import perf_counter_ns

def busqueda_lineal(a, x):
    ops = 0
    for i, valor in enumerate(a):
        ops += 1
        if valor == x:
            return i, ops
    return -1, ops

def busqueda_binaria(a, x):
    izq, der, ops = 0, len(a)-1, 0
    while izq <= der:
        medio = izq + (der-izq)//2
        ops += 1
        if a[medio] == x:
            return medio, ops
        if a[medio] < x:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, ops
