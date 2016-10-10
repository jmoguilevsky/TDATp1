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
        queue = deque([self.origin])
        
        found = False
        while not found:
            actual = queue.popleft()
            unmarkedAdjacents_e = filter(lambda x, m=marked: x.destiny not in m, self.graph.adj_e(actual))
            #unmarkedAdjacents = map(lambda x: x.destiny, unmarkedAdjacents_e)
            for node in unmarkedAdjacents_e:
                self.paths[node.destiny] = {'previous': actual, 'weight': node.weight}
                queue.append(node.destiny)
                marked.add(node.destiny)
                if node.destiny == self.destiny:
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