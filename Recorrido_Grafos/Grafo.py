# -*- coding: utf-8 -*-

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
    g.edges = {}
    g.vertices = V
    for v in xrange(V):
    	g.edges[v] = []

  def V(g):
    """Número de vértices en el grafo.
    """
    return g.vertices

  def E(g):
    """Número de aristas en el grafo.
    """
    return sum([len(g.edges[e]) for e in g.edges])

  def adj_e(g, v):
    """Itera sobre los aristas incidentes _desde_ v.
    """
    return iter(g.edges[v])

  def adj(g, v):
    """Itera sobre los vértices adyacentes a ‘v’.
    """
    return iter([e.destiny for e in g.edges[v]])

  def add_edge(g, u, v, weight=0):
    """Añade una arista al grafo.
    """
    g.edges[u].append(Edge(u,v,weight))

  def __iter__(g):
    """Itera de 0 a V."""
    return iter(xrange(g.V()))

  def iter_edges(g):
    """Itera sobre todas las aristas del grafo.

    Las aristas devueltas tienen los siguientes atributos de solo lectura:

        • e.src
        • e.dst
        • e.weight
    """
    return iter([x for e in g.edges for x in g.edges[e	]])

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