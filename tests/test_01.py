import unittest

from repartidor_01 import repartidor


class RepartidorTest(unittest.TestCase):
    def test_repartidor_greedy(self):
        grafo = [
            [0, 1, 2],
            [3, 0, 1],
            [1, 1, 0],
        ]
        resultado = repartidor(grafo)
        self.assertEqual([(0, 1), (1, 2), (2, 0)], resultado)

    def test_repartidor_4_nodos(self):
        grafo = [
            [0, 3, 4, 2],
            [3, 0, 5, 8],
            [4, 5, 0, 6],
            [2, 8, 6, 0]
        ]
        resultado = repartidor(grafo)
        self.assertEqual([(0, 3), (3, 2), (2, 1), (1, 0)], resultado)


if __name__ == '__main__':
    unittest.main()
