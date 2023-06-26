import unittest

from repartidor_02 import repartidor


class RepartidorRandomTest(unittest.TestCase):
    def test_repartidor_random(self):
        grafo = [
            [0, 3, 4, 2],
            [3, 0, 5, 8],
            [4, 5, 0, 6],
            [2, 8, 6, 0]
        ]
        resultado = repartidor(grafo)


if __name__ == '__main__':
    unittest.main()
