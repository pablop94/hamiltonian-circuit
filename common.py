def aristas(adyacentes):
    """
    Dado una lista de pesos devuelve una lista con sus aristas y su peso.
    """
    return [(j, peso) for j, peso in enumerate(adyacentes)]


def ordenar_por_peso(adyacentes):
    return sorted(adyacentes, key=lambda x: x[1])


def costo_camino(grafo, solucion):
    return sum(costo_arista(grafo, arista) for arista in solucion)


def costo_arista(grafo, arista):
    start, end = arista
    return grafo[start][end]
