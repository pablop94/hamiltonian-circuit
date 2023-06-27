# hamiltonian-circuit
Un ejemplo de circuito hamiltoniano usando grasp

## instalacion
```bash
pip install -r requirements.txt
```

## uso
```bash
python main.py
```

## configuración
Se pueden cambiar los grafos a generar, en el archivo `main.py` cambiar la variable `grafos_a_generar` por los grafos que se quieran generar, indicando la cantidad de nodos.

La idea es cambiar los parámetros con los mismos grafos y poder evaluar distintos resultados. Si se quisiese regenerar el conjunto de grafos, se puede cambiar la variable `regenerar` a `True`.

Además se puede cambiar la cantidad de resultados a randomizar por la parte greedy, actualmente en 2, cambiando la variable `mejores_n`.
