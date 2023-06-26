def aristas(adyacentes):
    """
    Dado una lista de pesos devuelve una lista con sus aristas y su peso.
    """
    return [(j, peso) for j, peso in enumerate(adyacentes)]


def ordenar_por_peso(adyacentes):
    return list(sorted(adyacentes, key=lambda x: x[1]))


def costo(grafo, solucion):
    return sum(grafo[start][end] for start, end in solucion)