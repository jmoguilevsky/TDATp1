# -*- coding: utf-8 -*-
from Vertice import *
from heapq import *

def relajar_vertice(heap,vertice1,vertice2,peso_arista):
	"""Función auxiliar que dado dos vertices y un peso determina si el valor de la distancia
	 mínima entre ellos debe ser actualizado; y en caso afirmativo lo actualiza."""
	d = vertice1.dist + peso_arista
	if d < vertice2.dist:
		vertice2.dist = d
		vertice2.padre = vertice1

def actualizar_heap(heap,vertice):
		"""Función auxiliar que dado un vertice actualiza el valor de su par asociado en la lista"""
		for par in heap:
			if par[1]==vertice:
				par[0]=vertice.dist
		heapify(heap)

def agregar_padres(lista_recorrido,vertice):
	"""Función auxiliar que dado un vértice agrega su padre a la lista y luego se llama recursivamente.
	La condición de corte es cuando el vértice dado no tiene padre."""
	dad = vertice.padre
	if dad != None:
		lista_recorrido.insert(0,dad.dato)
		agregar_padres(lista_recorrido,dad)

class Grafo(object):
	"""Clase que representa un Grafo mediante un diccionario de adyacencias"""
	def __init__(self):
		"""Crea una instancia de la clase sin vértices ni aristas y con el vértice central indefinido.
		El vértice central es aquel desde el cual se calculan las distancia ménimas a todos los demás vértices
		cuando se llama a Dijkstra."""
		self.vertices = {}
		self.conversion = {}
		self.vertice_central = None

	def agregar_vertice(self, dato):
		"""Primitiva que agrega un vértice al grafo"""
		vertice = Vertice(dato)
		self.conversion[dato] = vertice
		self.vertices[vertice] = []

	def agregar_arista(self,peso,dato1,dato2):
		"""Primitiva que agrega una arista al grafo.
		Si alguno de los vértices a unir no existe levanta una excepcion"""
		try:
			vertice1 = self.conversion[dato1]
			vertice2 = self.conversion[dato2]
			self.vertices[vertice1].append((peso,vertice2))
			self.vertices[vertice2].append((peso,vertice1))
		except KeyError:
			raise Exception("Uno de los vértices no existe")

	def dijkstra(self,vertice_inicial):
		"""Implementación del algoritmo de Dijkstra utilizando una cola de prioridad:
		calcula la distancia mínima a cada nodo desde el vértice dado."""
		#Inicializacion:
		self.vertice_central = vertice_inicial
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

	def camino_minimo(self,dato1,dato2):
		"""Primitiva que dados dos vértices"""
		try:
			vertice_inicial = self.conversion[dato1]
			vertice_final = self.conversion[dato2]
		except KeyError:
			raise Exception("Uno de los vértices no existe")

		if vertice_inicial != self.vertice_central: #Esto es si no se calculo Dijkstra desde el vertice pasado por parametro
			self.dijkstra(vertice_inicial)

		lista_recorrido = [] #Sera una lista de vertices en el orden del recorrido minimo
		distancia = vertice_final.dist
		lista_recorrido.insert(0,vertice_final.dato)
		agregar_padres(lista_recorrido,vertice_final)
		return lista_recorrido , distancia 

class Digraph(object):
  """Grafo no dirigido con un número fijo de vértices.

  Los vértices son siempre números enteros no negativos. El primer vértice
  es 0.

  El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
  creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
  nuevas aristas.
  """
  def __init__(g, V):
    """Construye un grafo sin aristas de V vértices.
    """
    g.vertices = V
    g.edges = []

  def V(g):
    """Número de vértices en el grafo.
    """
    return len(g.vertices)

  def E(g):
    """Número de aristas en el grafo.
    """
    return len(g.edges)

  def adj_e(g, v):
    """Itera sobre los aristas incidentes _desde_ v.
    """
    return iter([e.source for e in filter(lambda e: e.destiny == v, g.edges)])


  def adj(g, v):
    """Itera sobre los vértices adyacentes a ‘v’.
    """
    return iter([e.destiny for e in filter(lambda e: e.source == v, g.edges)])

  def add_edge(g, u, v, weight=0):
    """Añade una arista al grafo.
    """
    g.edges.append(Edge(u,v,weight))

  def __iter__(g):
    """Itera de 0 a V."""
    return iter(range(g.V()))

  def iter_edges(g):
    """Itera sobre todas las aristas del grafo.

    Las aristas devueltas tienen los siguientes atributos de solo lectura:

        • e.src
        • e.dst
        • e.weight
    """
    return iter(g.edges)

class Edge(object):
	"""Arista de un grafo.
	"""
  	def __init__(self, src, dst, weight):
		self.source = src
		self.destiny = dst
		self.weight = weight

	def __eq__(self, other):
		if (not isinstance(other, self.__class__) ) or other == None:
			return False
		return (self.source == other.source) and (self.destiny == other.destiny) and (self.weight == other.weight)

	def __cmp__(self, other):
		if other == None: return -1
		return (self.source == other.source) and (self.destiny == other.destiny) and (self.weight == other.weight)