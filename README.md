# hamiltonian-circuit
Un ejemplo de circuito hamiltoniano usando grasp

## instalacion
```bash
pip install -r requirements.txt
```

## uso
```bash
python main.py N [N...] [--bestn 2] [-g]
```

### detalles
Al comando se le pasan la cantidad de nodos de los grafos a analizar, pueden ser varios.

Si queremos generar grafos nuevos usamos `-g`.

Si queremos modificar la cantidad de elementos que toma el greedy para randomizar, podemos usar
el parámetro `--bestn`.
