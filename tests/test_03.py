import unittest

from repartidor_03 import busqueda_local


class BusquedaLocalTest(unittest.TestCase):
    def test_mejora_busqueda_local(self):
        grafo = [
            [0, 3, 4, 2],
            [3, 0, 5, 8],
            [4, 5, 0, 6],
            [2, 8, 6, 0]
        ]
        resultado = [(2, 1), (1, 3), (3, 0), (0, 2)]

        self.assertEqual([(2, 1), (1, 0), (0, 3), (3, 2)], busqueda_local(grafo, resultado))


if __name__ == '__main__':
    unittest.main()
