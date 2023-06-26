from common import ordenar_por_peso, aristas


def repartidor(grafo):
    """
    Dado un grafo, voy a recorrer sus nodos y para cada nodo voy a tomar la arista con menor
    peso que no haya sido visitada.
    """
    inicial = 0
    actual = inicial
    resultado = []
    visitados = {actual}

    while len(visitados) != len(grafo):
        for arista, peso in ordenar_por_peso(aristas(grafo[actual])):
            if arista not in visitados and arista != actual:
                visitados.add(arista)
                resultado.append((actual, arista))
                actual = arista
                break

    resultado.append((actual, inicial))
    return resultado
