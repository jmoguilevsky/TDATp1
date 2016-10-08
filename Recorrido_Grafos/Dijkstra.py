from AlgoritmoDeRecorrido import *
from heapq import *

class Dijkstra(Algorithm):

	def __init__(self, g, origin, destiny, heuristic = None):
		super(Dijkstra, self).__init__(g, origin, destiny)


	def dijkstra(self):
		"""Implementación del algoritmo de Dijkstra utilizando una cola de prioridad:
		calcula la distancia mínima a cada nodo desde el vértice dado."""
		#Inicializacion:
		lista_tratados = []
		heap = []
		for clave,valor in self.vertices.iteritems():
			if clave == vertice_inicial:
				vertice_inicial.dist=0
				vertice_inicial.padre=None
			else:
				clave.dist = float("inf") #Representa el infinito en python, todo otro numero sera menor
			heappush(heap,[clave.dist,clave]) #Se encola la distancia para que la cola pueda comparar los elementos

		#Comienza el algoritmo
		while heap:
			l = heappop(heap) #l es [vertice.dist,vertice]
			vertice = l[1]
			lista_tratados.append(vertice)
			for adyacente in self.vertices[vertice]: #adyacente es (peso,arista)
				relajar_vertice(heap,vertice,adyacente[1],adyacente[0])
				actualizar_heap(heap,adyacente[1])
		