from common import costo_camino


def busqueda_local(grafo, solucion):
    costo_actual = costo_camino(grafo, solucion)

    posible_mejora = solucion.copy()
    fin_anterior = None
    next_index = 0
    for i, (inicio, fin) in enumerate(solucion):
        if fin_anterior is not None and i > next_index:
            posible_mejora[i-1] = posible_mejora[i-1][0], fin
            posible_mejora[i] = fin, fin_anterior
            next_index = (i+1) % len(posible_mejora)
            posible_mejora[next_index] = fin_anterior, posible_mejora[next_index][1]
            nuevo_costo = costo_camino(grafo, posible_mejora)
            if costo_actual > nuevo_costo:
                costo_actual = nuevo_costo
            else:
                posible_mejora[i-1] = solucion[i-1]
                posible_mejora[i] = solucion[i]
                posible_mejora[next_index] = solucion[next_index]
                next_index = i
        fin_anterior = fin

    return posible_mejora
