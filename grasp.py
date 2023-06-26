import json
import math
import matplotlib.pyplot as plt

from common import costo
from repartidor_02 import repartidor
from repartidor_03 import busqueda_local


def grasp(grafo, loops, mejores_n):
    costo_actual = math.inf
    resultado = None

    i = 0
    while i < loops:
        resultado_parcial = busqueda_local(grafo, repartidor(grafo, mejores_n=mejores_n))
        nuevo_costo = costo(grafo, resultado_parcial)
        if nuevo_costo < costo_actual:
            resultado = resultado_parcial
            costo_actual = nuevo_costo

        i += 1

    return costo_actual, resultado


if __name__ == '__main__':
    with open("input.json", "r") as file:
        grafo = json.load(file)
        start_loops = 1
        increment = 1
        limit = 100
        x = []
        y = []

        while start_loops < limit:
            result = grasp(grafo, start_loops)
            x.append(start_loops)
            y.append(result[0])
            start_loops += increment

        plt.plot(x, y)
        plt.savefig(f"resultados/grasp-{len(grafo)}.png")
        plt.close()
