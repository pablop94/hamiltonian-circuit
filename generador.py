import json
import random


def generar_grafo(n, max_cost):
    matriz_costos = [[random.randint(1, max_cost) for _ in range(n)] for _ in range(n)]

    # Asignar un valor alto a la diagonal principal para evitar ciclos
    for i in range(n):
        matriz_costos[i][i] = 0

    return matriz_costos


def generar(n, max_cost=5):
    matriz = generar_grafo(n, max_cost)
    with open("input.json", "w") as file:
        file.write(json.dumps(matriz))


if __name__ == '__main__':
    generar(8, 5)
