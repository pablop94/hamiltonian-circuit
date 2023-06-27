import json
import os.path

from matplotlib import pyplot as plt

from generador import generar
from graph_draw import draw_graph
from grasp import grasp


def validate_file(file_name):
    if not os.path.exists(file_name):
        print("No existen los grafos de input, cambia la variable generar_grafos a True para crearlos")
        exit(1)


if __name__ == '__main__':
    mejores_n = 2
    # Indico los grafos a generar según su cantidad de nodos
    grafos_a_generar = [5, 10, 20]
    regenerar = False

    for n in grafos_a_generar:
        if regenerar:
            print(f"Generando grafo de {n} nodos")
            generar(n)

        filename = f"inputs/input{n}.json"

        validate_file(filename)

        with open(filename, "r") as file:
            grafo = json.load(file)
            loops = n
            incremento = n * 10
            limite = (n ** 2) * 10
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

        if len(grafo) < 10:
            draw_graph(grafo, result[1])
