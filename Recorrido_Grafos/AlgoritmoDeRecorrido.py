from Grafo import *

class Algorithm(object):
	"""  """
	def __init__(self, g, origin, destiny, heuristic = None):
		self.graph = g
		self.origin = origin
		self.destiny = destiny
		self.heuristic = heuristic
		self.road = []
		self.algorithm()
		self.generate_road()

	def visited(self, v):
		return v in self.road

	def distance(self, v):
		if not self.visited(v):
			return float("inf")
		return self.getDistance(v)

	def camino(self, v):
		if not self.visited(v):
			return None
		return self.road[0:self.road.index(v)]