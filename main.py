import json

from matplotlib import pyplot as plt

from generador import generar
from grasp import grasp

if __name__ == '__main__':

    for n in [8, 10, 20]:
        print(f"Generando grafo de {n} nodos")
        generar(n)
        with open("input.json", "r") as file:
            grafo = json.load(file)
            start_loops = n
            increment = n
            limit = n * 100
            x = []
            y = []
            print(f"Calculando camino hamiltoniano minimo desde {start_loops} repeticiones, incremento de {increment}"
                  f" y limite de {limit}")
            while start_loops < limit:
                result = grasp(grafo, start_loops)
                x.append(start_loops)
                y.append(result[0])
                start_loops += increment
            print("Graficando resultados")
            plt.plot(x, y)
            plt.savefig(f"resultados/grasp-{len(grafo)}.png")
            plt.close()
