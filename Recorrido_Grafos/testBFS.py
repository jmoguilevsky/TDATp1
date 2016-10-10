import unittest
from Grafo import Grafo
from BFS import *

class BFSTest(unittest.TestCase):

    def setUp(self):
        self.graph = Grafo.Grafo()
        self.graph.agregar_vertice(0)
        self.graph.agregar_vertice(1)
        self.graph.agregar_vertice(2)
        self.graph.agregar_vertice(3)
        self.graph.agregar_vertice(4)

        self.graph.agregar_arista(10, 0, 1)
        self.graph.agregar_arista(20, 1, 4)
        self.graph.agregar_arista( 1, 0, 2)
        self.graph.agregar_arista( 2, 2, 3)
        self.graph.agregar_arista( 3, 3, 4)

        self.bfs = BFS(self.graph, 0, 4)
        

    def test_createAlgorithm(self):
        graph = Grafo.Grafo()
        graph.agregar_vertice(0)
        graph.agregar_vertice(1)
        graph.agregar_arista(1, 0, 1)
        bfs = BFS(graph, 0, 1)
        self.assertIsNotNone(bfs)

    def test_CaseOne(self):
        self.assertEqual(self.bfs.distance(4), 30)

    def test_CaseTwo(self):
        self.assertEqual(self.bfs.distance(3), float("inf"))

    def test_CaseThree(self):
        self.assertEqual(self.bfs.distance(1), 10)

    def test_camino(self):
        self.assertEqual(self.bfs.camino(4), [0, 1])
        self.assertEqual(self.bfs.camino(1), [0])

    def test_visited(self):
        self.assertFalse(self.bfs.visited(3))
        self.assertFalse(self.bfs.visited(2))
        self.assertTrue(self.bfs.visited(4))


    def test_EdgeTo(self):
        self.assertEqual(self.bfs._edge_to(4), 1)

if __name__ == '__main__':
    unittest.main()