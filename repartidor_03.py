from common import costo_camino, costo_arista


def busqueda_local(grafo, solucion):
    costo_actual = costo_camino(grafo, solucion)

    posible_mejora = solucion.copy()
    fin_anterior = None
    proximo_indice = 0
    for i, (inicio, fin) in enumerate(solucion):
        if fin_anterior is not None and i > proximo_indice:
            posible_mejora[i-1] = posible_mejora[i-1][0], fin
            posible_mejora[i] = fin, fin_anterior
            proximo_indice = (i+1) % len(posible_mejora)
            posible_mejora[proximo_indice] = fin_anterior, posible_mejora[proximo_indice][1]

            costo_indices_en_actual = costo_indices(grafo, solucion, i-1, i, proximo_indice)
            costo_indices_en_mejora = costo_indices(grafo, posible_mejora, i-1, i, proximo_indice)
            nuevo_costo = costo_actual - costo_indices_en_actual + costo_indices_en_mejora

            if costo_actual > nuevo_costo:
                costo_actual = nuevo_costo
            else:
                posible_mejora[i-1] = solucion[i-1]
                posible_mejora[i] = solucion[i]
                posible_mejora[proximo_indice] = solucion[proximo_indice]
                proximo_indice = i

        fin_anterior = fin

    return posible_mejora


def costo_indices(grafo, camino, *indices):
    """
    Dado un grafo, un camino y una lista de indices, devuelve el costo de las aristas en las posiciones de los indices
    """
    return sum(costo_arista(grafo, camino[i]) for i in indices)
