import unittest
from Grafo import Digraph
from Dijkstra import *

class DijkstraTest(unittest.TestCase):

	def test_createAlgorithm(self):
		graph = Digraph(4)
		dijkstra = Dijkstra(graph, 2, 1)
		self.assertIsNotNone(dijkstra)
		
if __name__ == '__main__':
	unittest.main()