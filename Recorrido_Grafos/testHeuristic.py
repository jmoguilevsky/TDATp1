import unittest
from Grafo import Digraph
from Heuristic import *

def heuristicF(a,b):
	(x1, y1) = a
	(x2, y2) = b
	return 1 * (abs(x1 - x2) + abs(y1 - y2))

class HeuristicTest(unittest.TestCase):

	def setUp(self):
		self.graph = Digraph(9)
		self.graph.add_edge(0,1,2)
		self.graph.add_edge(0,3,2)
		self.graph.add_edge(1,0,2)
		self.graph.add_edge(1,4,2)
		self.graph.add_edge(1,2,2)
		self.graph.add_edge(2,1,2)
		self.graph.add_edge(2,5,2)
		self.graph.add_edge(3,0,2)
		self.graph.add_edge(3,4,2)
		self.graph.add_edge(3,6,2)
		self.graph.add_edge(4,1,2)
		self.graph.add_edge(4,3,2)
		self.graph.add_edge(4,5,2)
		self.graph.add_edge(4,7,2)
		self.graph.add_edge(5,2,2)
		self.graph.add_edge(5,4,2)
		self.graph.add_edge(5,8,2)
		self.graph.add_edge(6,3,2)
		self.graph.add_edge(6,7,2)
		self.graph.add_edge(7,6,2)
		self.graph.add_edge(7,4,2)
		self.graph.add_edge(7,8,2)
		self.graph.add_edge(8,5,2)
		self.graph.add_edge(8,7,2)
		self.vertexToXY = {
			0: (0,0),
			1: (1,0),
			2: (2,0),
			3: (0,1),
			4: (1,1),
			5: (2,1),
			6: (0,2),
			7: (1,2),
			8: (2,2)
		}
		"""
		0 1 2
		3 4 5
        6 7 8
		"""
		self.heuristic = Heuristic(self.graph, 0, 8, self.vertexToXY, heuristicF)
		

	def test_createAlgorithm(self):
		graph = Digraph(4)
		graph.add_edge(0,1,2)
		graph.add_edge(0,2,2)
		graph.add_edge(0,3,2)
		#heuristic = Heuristic(graph, 2, 1, self.vertexToXY, heuristicF)
		#self.assertIsNotNone(heuristic)

	def test_CaseOne(self):
		print(self.heuristic.road)
		print(self.heuristic.vertices)
		self.assertEqual(self.heuristic.distance(8), 4)

#	def test_CaseTwo(self):
#		self.assertEqual(self.dijkstra.distance(4), float("inf"))
#
#	def test_CaseThree(self):
#		self.assertEqual(self.dijkstra.distance(1), 2)
#
#	def test_EdgeTo(self):
#		self.assertEqual(self.dijkstra._edge_to(8), 1)


if __name__ == '__main__':
	unittest.main()