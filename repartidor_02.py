import random

from common import ordenar_por_peso, aristas


def repartidor(grafo):
    return repartidor_random(grafo, inicial=random.choice(range(len(grafo))))


def repartidor_random(grafo, inicial=0):
    """
    Dado un grafo, voy a recorrer sus nodos y para cada nodo voy a tomar la arista con menor
    peso que no haya sido visitada.
    """
    actual = inicial
    resultado = []
    visitados = {actual}

    while len(visitados) != len(grafo):
        count = 0
        for arista, peso in ordenar_por_peso(aristas(grafo[actual])):
            moneda = random.choice([True, False])

            if arista not in visitados and arista != actual and (moneda or count == len(grafo)-1):
                visitados.add(arista)
                resultado.append((actual, arista))
                actual = arista
                break
            count += 1

    resultado.append((actual, inicial))
    return resultado
