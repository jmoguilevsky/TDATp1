import unittest
from Grafo import Digraph
from Dijkstra import *

class DijkstraTest(unittest.TestCase):

	def setUp(self):
		self.graph = Digraph(10)
		self.graph.add_edge(0,1,2)
		self.graph.add_edge(0,2,2)
		self.graph.add_edge(1,4,2)
		self.graph.add_edge(2,5,2)
		self.graph.add_edge(3,6,2)
		self.graph.add_edge(4,7,2)
		self.graph.add_edge(1,8,2)
		self.graph.add_edge(2,8,4)
		self.graph.add_edge(6,8,2)
		self.dijkstra = Dijkstra(self.graph, 0, 8)
		

	def test_createAlgorithm(self):
		graph = Digraph(4)
		graph.add_edge(0,1,2)
		graph.add_edge(0,2,2)
		graph.add_edge(0,3,2)
		dijkstra = Dijkstra(graph, 2, 1)
		self.assertIsNotNone(dijkstra)

	def test_CaseOne(self):
		self.assertEqual(self.dijkstra.distance(8), 4)

	def test_CaseTwo(self):
		self.assertEqual(self.dijkstra.distance(4), float("inf"))

	def test_CaseThree(self):
		self.assertEqual(self.dijkstra.distance(1), 2)

if __name__ == '__main__':
	unittest.main()