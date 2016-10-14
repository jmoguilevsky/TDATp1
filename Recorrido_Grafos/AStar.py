from AlgoritmoDeRecorrido import *
from heapq import *

def heuristicF(a,b):
	(x1, y1) = a
	(x2, y2) = b
	return 10000 * (abs(x1 - x2) + abs(y1 - y2))

def actualizar_heap(heap,vertice, parVertice):
	"""Funcion auxiliar que dado un vertice actualiza el valor de su par asociado en la lista"""
	for par in heap:
		if par[1]==vertice:
			par[0]=parVertice["dist"]
			break
	heapify(heap)


class AStar(Algorithm):

	def __init__(self, g, origin, destiny, vertexToXYMap, heuristic):
		self.vertices = {}
		super(AStar, self).__init__(g, origin, destiny, vertexToXYMap, heuristic)


	def mappedHeuristic(self, origin, destination):
		return self.heuristic(self.vertexToXYMap[origin], self.vertexToXYMap[destination])

	def generate_road(self):
		"""Funcion auxiliar que dado un vertice agrega sus previos a la lista.
		"""
		previous = self.vertices[self.destiny]["previous"]
		self.road.append(self.destiny)
		while previous != None:
			self.road.insert(0,previous)
			previous = self.vertices[previous]["previous"]

	def relajar_vertice(self,adjacentEdges, vertex):
		"""Funcion auxiliar que dado dos vertices y un peso determina si el valor de la distancia
		minima entre ellos debe ser actualizado; y en caso afirmativo lo actualiza."""
		d = self.heuristic(self.vertexToXYMap[vertex], self.vertexToXYMap[self.destiny])
		self.vertices[vertex]["dist"] = self.vertices[vertex]['dist']
		adjacentEdges.append(vertex)
			


	def algorithm(self):
		"""Implementacion del algoritmo de Dijkstra utilizando una cola de prioridad:
		calcula la distancia minima a cada nodo desde el vertice dado."""
		#Inicializacion:
		listOfVertices = []
		self.vertices = {}
		for v in self.graph:
			self.vertices[v] = {"dist": float('inf'), "previous": None}
			if v == self.origin:
				self.vertices[v]["dist"] = 0
		
		# Comienza el algoritmo
		# verticesQueue guarda una lista de (peso, vertice).
		#	heappop() se encarga de popear el de menor peso de toda la lista
		verticesQueue = [(0, self.origin)]
		markedVertices = [self.origin]
		while verticesQueue:
			vertex = heappop(verticesQueue)[1]
			print 'vertex', vertex
			if vertex == self.destiny:
				break

			adjacentEdges = self.graph.adj_e(vertex)
			verticesToVisit = filter(lambda e, m=markedVertices: (e.destiny not in m), adjacentEdges)
			print 'toVisit', [str(e) for e in verticesToVisit]
			for edge in verticesToVisit:
				heuristicValue = self.mappedHeuristic(edge.destiny, self.destiny)
				newCost = self.vertices[vertex]['dist'] + edge.weight
				heappush( verticesQueue, (heuristicValue + newCost, edge.destiny) )
				self.vertices[edge.destiny] = {'previous': vertex, 'dist': newCost}
				markedVertices.append(edge.destiny)

			print 'asi quedo la q', [str(e) for e in verticesQueue]


		print self.vertices


	def getDistance(self, v):
		return self.vertices[v]["dist"]

	
def mainTests():
	graph = Digraph(9)
	graph.add_edge(0,1,20)
	graph.add_edge(0,3,2)
	graph.add_edge(1,0,2)
	graph.add_edge(1,4,2)
	graph.add_edge(1,2,20)
	graph.add_edge(2,1,2)
	graph.add_edge(2,5,20)
	graph.add_edge(3,0,2)
	graph.add_edge(3,4,2)
	graph.add_edge(3,6,2)
	graph.add_edge(4,1,2)
	graph.add_edge(4,3,2)
	graph.add_edge(4,5,2)
	graph.add_edge(4,7,2)
	graph.add_edge(5,2,2)
	graph.add_edge(5,4,2)
	graph.add_edge(5,8,20)
	graph.add_edge(6,3,2)
	graph.add_edge(6,7,2)
	graph.add_edge(7,6,2)
	graph.add_edge(7,4,2)
	graph.add_edge(7,8,2)
	graph.add_edge(8,5,2)
	graph.add_edge(8,7,2)


	"""
	The following graph connects this way:
	0 - 1 - 8
	|   |   |
	7 - 5 - 4
	|   |   |
	2 - 6 - 3

	This is a perfect example where the numbers in every vertex
	mean nothing, so the heuristic will make a nonsense guess.
	The algorithm will wrongly find the path from 0 to 8 as [0, 7, 5, 4, 8]
	"""
	"""
	graph.add_edge(0, 1, 1)
	graph.add_edge(0, 7, 1)
	graph.add_edge(1, 0, 1)
	graph.add_edge(1, 8, 1)
	graph.add_edge(1, 5, 1)
	graph.add_edge(8, 1, 1)
	graph.add_edge(8, 4, 1)
	graph.add_edge(7, 0, 1)
	graph.add_edge(7, 5, 1)
	graph.add_edge(7, 2, 1)
	graph.add_edge(5, 1, 1)
	graph.add_edge(5, 7, 1)
	graph.add_edge(5, 6, 1)
	graph.add_edge(5, 4, 1)
	graph.add_edge(4, 5, 1)
	graph.add_edge(4, 8, 1)
	graph.add_edge(4, 3, 1)
	graph.add_edge(2, 7, 1)
	graph.add_edge(2, 6, 1)
	graph.add_edge(6, 2, 1)
	graph.add_edge(6, 5, 1)
	graph.add_edge(6, 3, 1)
	graph.add_edge(3, 6, 1)
	graph.add_edge(3, 4, 1)
	"""

	vertexToXY = {
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
	aStar = AStar(graph, 0, 8, vertexToXY, heuristicF)
	print(aStar.vertices)
	print(aStar.camino(8))

	

if __name__ == '__main__':
	mainTests()
		