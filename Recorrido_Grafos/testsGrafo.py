import unittest
from Grafo import Digraph, Edge

class GrafoTest(unittest.TestCase):
	def setUp(self):
		self.graph = Digraph([0,1,2,3])

	def test_createGraph(self):
		graph = Digraph([0,1,2,3])
		self.assertIsNotNone(graph)

	def test_sizeIsTheSameAsCreated(self):
		self.assertEqual(self.graph.V(), 4)

	def test_addEdge(self):
		self.graph.add_edge(0,1,2)
		self.assertEqual(self.graph.E(), 1)

	def test_adjacentsOfVertex(self):
		self.graph.add_edge(0,1,2)
		self.graph.add_edge(0,2,2)
		self.graph.add_edge(0,3,2)
		self.assertEqual(list(self.graph.adj(0)), [1,2,3])

	def test_adjacentsFromVertex(self):
		self.graph.add_edge(0,1,2)
		self.graph.add_edge(1,2,2)
		self.graph.add_edge(2,1,2)
		self.assertEqual(list(self.graph.adj_e(1)), [0, 2])

	def test_iterEdges(self):
		e1 = Edge(0,1,2)
		e2 = Edge(1,2,2)
		e3 = Edge(2,1,2)
		edges = [e1,e2,e3]
		self.graph.add_edge(0,1,2)
		self.graph.add_edge(1,2,2)
		self.graph.add_edge(2,1,2)
		self.assertEqual(list(self.graph.iter_edges()), edges)

#	def test_goingSouthThrowsException(self):
#		self.rover.processMovement(TURNRIGHT)
#		with self.assertRaises(Exception):
#			self.rover.processMovement(MOVE)

if __name__ == '__main__':
	unittest.main()