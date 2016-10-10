from AlgoritmoDeRecorrido import *
from heapq import *

def heuristicF(a,b):
	(x1, y1) = a
	(x2, y2) = b
	return 1 * (abs(x1 - x2) + abs(y1 - y2))

def actualizar_heap(heap,vertice, parVertice):
		"""Funcion auxiliar que dado un vertice actualiza el valor de su par asociado en la lista"""
		for par in heap:
			if par[1]==vertice:
				par[0]=parVertice["dist"]
				break
		heapify(heap)


class Heuristic(Algorithm):

	def __init__(self, g, origin, destiny, vertexToXYMap, heuristic):
		self.vertices = {}
		super(Heuristic, self).__init__(g, origin, destiny, vertexToXYMap, heuristic)


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
		d = self.heuristic(self.vertexToXYMap[e.destiny], self.vertexToXYMap[self.destiny])
		if d < self.vertices[vertex]:
			self.vertices[vertex]["dist"] = d
		adjacentEdges.append(vertex)
			


	def algorithm(self):
		"""Implementacion del algoritmo de Dijkstra utilizando una cola de prioridad:
		calcula la distancia minima a cada nodo desde el vertice dado."""
		#Inicializacion:
		listOfVertices = []
		self.vertices = {}
		for v in self.graph:
			self.vertices[v] = {"dist": 0, "previous": None}
			if v == self.origin:
				self.vertices[v]["dist"]=0
				self.vertices[v]["previous"]=None
				listOfVertices.append(v)
			else:
				self.vertices[v]["dist"] = float("inf") #Representa el infinito en python, todo otro numero sera menor
		print('pre',self.vertices)
		#Comienza el algoritmo

		while listOfVertices:
			vertex = listOfVertices.pop()
			if vertex == self.destiny:
				break
			print('vertex', vertex)
			print('adj', [str(e) for e in self.graph.adj_e(vertex)])
			adjacentEdges = []
			for e in self.graph.adj_e(vertex): #adyacente es Edge
				self.relajar_vertice(adjacentEdges, e.destiny)
				
			adjacentEdges.sort()
			[listOfVertices.insert(0, e[1]) for e in adjacentEdges]


	def getDistance(self, v):
		return self.vertices[v]["dist"]

	
def mainTests():
	graph = Digraph(9)
	graph.add_edge(0,1,2)
	graph.add_edge(0,3,2)
	graph.add_edge(1,0,2)
	graph.add_edge(1,4,2)
	graph.add_edge(1,2,2)
	graph.add_edge(2,1,2)
	graph.add_edge(2,5,2)
	graph.add_edge(3,0,2)
	graph.add_edge(3,4,2)
	graph.add_edge(3,6,2)
	graph.add_edge(4,1,2)
	graph.add_edge(4,3,2)
	graph.add_edge(4,5,2)
	graph.add_edge(4,7,2)
	graph.add_edge(5,2,2)
	graph.add_edge(5,4,2)
	graph.add_edge(5,8,2)
	graph.add_edge(6,3,2)
	graph.add_edge(6,7,2)
	graph.add_edge(7,6,2)
	graph.add_edge(7,4,2)
	graph.add_edge(7,8,2)
	graph.add_edge(8,5,2)
	graph.add_edge(8,7,2)
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
	heuristic = Heuristic(graph, 0, 8, vertexToXY, heuristicF)
	print(heuristic.vertices)
	print(heuristic.camino(8))

	

if __name__ == '__main__':
	mainTests()
		