from AlgoritmoDeRecorrido import *
from heapq import *

def relajar_vertice(heap,vertice1, parVertice1, parVertice2,peso_arista):
	"""Funcion auxiliar que dado dos vertices y un peso determina si el valor de la distancia
	minima entre ellos debe ser actualizado; y en caso afirmativo lo actualiza."""
	d = parVertice1["dist"] + peso_arista
	if d < parVertice2["dist"]:
		parVertice2["dist"] = d
		parVertice2["padre"] = vertice1

def actualizar_heap(heap,vertice, parVertice):
		"""Funcion auxiliar que dado un vertice actualiza el valor de su par asociado en la lista"""
		for par in heap:
			if par[1]==vertice:
				par[0]=parVertice["dist"]
				break
		heapify(heap)


class Dijkstra(Algorithm):

	def __init__(self, g, origin, destiny, heuristic = None):
		super(Dijkstra, self).__init__(g, origin, destiny)
		self.dijkstra()



	def dijkstra(self):
		"""Implementacion del algoritmo de Dijkstra utilizando una cola de prioridad:
		calcula la distancia minima a cada nodo desde el vertice dado."""
		#Inicializacion:
		heap = []
		vertices = {}
		for v in self.graph:
			vertices[v] = {"dist": 0, "previous": None}
			if v == self.origin:
				vertices[v]["dist"]=0
				vertices[v]["padre"]=None
			else:
				vertices[v]["dist"] = float("inf") #Representa el infinito en python, todo otro numero sera menor
			heappush(heap,[vertices[v]["dist"],v]) #Se encola la distancia para que la cola pueda comparar los elementos

		#Comienza el algoritmo
		while heap:
			l = heappop(heap) #l es [vertice.dist,vertice]
			vertice = l[1]
			self.road.append(vertice)
			for e in self.graph.adj_e(vertice): #adyacente es Arista
				relajar_vertice(heap, vertice, vertices[vertice], vertices[e.destiny], e.weight)
				actualizar_heap(heap,vertice, vertices[vertice])
		