import random

from common import ordenar_por_peso, aristas


def repartidor(grafo, mejores_n):
    return repartidor_random(grafo, inicial=random.choice(range(len(grafo))), mejores_n=mejores_n)


def repartidor_random(grafo, inicial=0, mejores_n=4):
    """
    Dado un grafo, voy a recorrer sus nodos y para cada nodo voy a tomar la arista con menor
    peso que no haya sido visitada.
    """
    actual = inicial
    resultado = []
    visitados = {actual}

    while len(visitados) != len(grafo):
        aristas_validas = [arista for arista, peso in ordenar_por_peso(aristas(grafo[actual])) if arista not in visitados and arista != actual]

        arista = random.choice(aristas_validas[:mejores_n])
        visitados.add(arista)
        resultado.append((actual, arista))
        actual = arista

    resultado.append((actual, inicial))
    return resultado
