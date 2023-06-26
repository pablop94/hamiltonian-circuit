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
            loops = n
            incremento = n * 10
            limite = (n ** 2) * 10
            mejores_n = 2
            x = []
            y = []
            print(f"Calculando camino hamiltoniano minimo desde {loops} repeticiones, incremento de {incremento}"
                  f" y limite de {limite}. Greedy entre los mejores {mejores_n}")
            while loops < limite:
                result = grasp(grafo, loops, mejores_n)
                x.append(loops)
                y.append(result[0])
                loops += incremento
            print("Graficando resultados")
            plt.plot(x, y)
            plt.savefig(f"resultados/grasp-{len(grafo)}.png")
            plt.close()
