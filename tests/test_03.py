import unittest

from repartidor_02 import repartidor
from repartidor_03 import busqueda_local


class MyTestCase(unittest.TestCase):
    def test_something(self):
        grafo = [
            [0, 3, 4, 2],
            [3, 0, 5, 8],
            [4, 5, 0, 6],
            [2, 8, 6, 0]
        ]
        resultado = repartidor(grafo)

        busqueda_local(grafo, resultado)


if __name__ == '__main__':
    unittest.main()
