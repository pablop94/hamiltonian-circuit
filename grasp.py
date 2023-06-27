import json
import math
import matplotlib.pyplot as plt

from common import costo_camino
from repartidor_02 import repartidor
from repartidor_03 import busqueda_local


def grasp(grafo, loops, mejores_n):
    costo_actual = math.inf
    resultado = None

    i = 0
    while i < loops:
        resultado_parcial = busqueda_local(grafo, repartidor(grafo, mejores_n=mejores_n))
        nuevo_costo = costo_camino(grafo, resultado_parcial)
        if nuevo_costo < costo_actual:
            resultado = resultado_parcial
            costo_actual = nuevo_costo

        i += 1

    return costo_actual, resultado
