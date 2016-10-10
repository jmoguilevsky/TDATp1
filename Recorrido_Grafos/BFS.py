from collections import deque
from sets import Set
import Grafo
from AlgoritmoDeRecorrido import Algorithm

class BFS(Algorithm):

    def __init__(self, g, origin, dest, heuristic = None):
        self.paths = {}
        super(BFS, self).__init__(g, origin, dest, heuristic)
        
    def algorithm(self):
        marked = Set([self.origin])
        queue = deque([(0, self.origin)])
        
        found = False
        while not found:
            actual = queue.popleft()
            unmarkedAdjacents = filter(lambda x, m=marked: x[1] not in m, self.graph.adyacentes(actual[1]))
            for node in unmarkedAdjacents:
                self.paths[node[1]] = {'previous': actual[1], 'weight': node[0]}
                queue.append(node)
                marked.add(node[1])
                if node[1] == self.destiny:
                    return


    def generate_road(self):
        self.road = []
        self.weights = []

        actual = self.destiny
        while actual != self.origin:
            self.road.insert(0, actual)
            self.weights.insert(0, self.paths[actual]['weight'])
            actual = self.paths[actual]['previous']
        self.road.insert(0, self.origin)


    def getDistance(self, v):
        if v in self.road:
            return sum(self.weights[:self.road.index(v)])
        else:
            return float('inf')