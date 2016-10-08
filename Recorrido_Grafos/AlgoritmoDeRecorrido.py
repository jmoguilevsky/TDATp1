from Grafo import *

class Algorithm(object):
	"""  """
	def __init__(self, g, origin, destiny, heuristic = None):
		self.graph = g
		self.origin = origin
		self.destiny = destiny
		self.heuristic = heuristic

	def visited(self, v):
		return True

	def distance(self, v):
		return 1

	def camino(self, v):
		return []