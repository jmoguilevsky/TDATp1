from Grafo import *

class Algorithm(object):
	"""  """
	def __init__(self, g, origin, destiny, vertexToXYMap = None, heuristic = None):
		"""
		heurisic has to be heuristic(a,b) where a,b are a = [x,y] a position in a 'map'
		"""
		self.graph = g
		self.origin = origin
		self.destiny = destiny
		self.heuristic = heuristic
		self.vertexToXYMap = vertexToXYMap
		self.road = []
		self.algorithm()
		self.generate_road()

	def visited(self, v):
		return v in self.road

	def distance(self, v):
		if not self.visited(v):
			return float("inf")
		return self.getDistance(v)

	def _edge_to(self, v):
		if not self.visited(v):
			return float("inf")
		return self.road[self.road.index(v) - 1]

	def camino(self, v):
		if not self.visited(v):
			return None
		return self.road[0:self.road.index(v)]