from AlgoritmoDeRecorrido import *
from heapq import *

def actualizar_heap(heap,vertice, parVertice):
		"""Funcion auxiliar que dado un vertice actualiza el valor de su par asociado en la lista"""
		for par in heap:
			if par[1]==vertice:
				par[0]=parVertice["dist"]
				break
		heapify(heap)


class Dijkstra(Algorithm):

	def __init__(self, g, origin, destiny, vertexToXYMap = None, heuristic = None):
		self.vertices = {}
		super(Dijkstra, self).__init__(g, origin, destiny)

	def generate_road(self):
		"""Funcion auxiliar que dado un vertice agrega sus previos a la lista.
		"""
		previous = self.vertices[self.destiny]["previous"]
		self.road.append(self.destiny)
		while previous != None:
			self.road.insert(0,previous)
			previous = self.vertices[previous]["previous"]

	def relajar_vertice(self, heap,vertice1, parVertice1, parVertice2,peso_arista):
		"""Funcion auxiliar que dado dos vertices y un peso determina si el valor de la distancia
		minima entre ellos debe ser actualizado; y en caso afirmativo lo actualiza."""
		d = parVertice1["dist"] + peso_arista
		if d < parVertice2["dist"]:
			parVertice2["dist"] = d
			parVertice2["previous"] = vertice1


	def algorithm(self):
		"""Implementacion del algoritmo de Dijkstra utilizando una cola de prioridad:
		calcula la distancia minima a cada nodo desde el vertice dado."""
		#Inicializacion:
		heap = []
		self.vertices = {}
		for v in self.graph:
			self.vertices[v] = {"dist": 0, "previous": None}
			if v == self.origin:
				self.vertices[v]["dist"]=0
				self.vertices[v]["previous"]=None
			else:
				self.vertices[v]["dist"] = float("inf") #Representa el infinito en python, todo otro numero sera menor
			heappush(heap,[self.vertices[v]["dist"],v]) #Se encola la distancia para que la cola pueda comparar los elementos

		#Comienza el algoritmo

		while heap:
			v = heappop(heap)
			vertex = v[1]
			for e in self.graph.adj_e(vertex): #adyacente es Edge
				self.relajar_vertice(heap, vertex, self.vertices[vertex], self.vertices[e.destiny], e.weight)
				actualizar_heap(heap,vertex, self.vertices[vertex])

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
	dijkstra = Dijkstra(graph, 0, 8)
	print(dijkstra.camino(8))
	print(dijkstra.vertices)
	

if __name__ == '__main__':
	mainTests()
		