from collections import deque
from sets import Set
import Grafo


def pathTo(dest, paths):
    edgesPath = []
    actual = dest
    while actual in paths:
        edgesPath.insert(0, (paths[actual], actual))
        actual = paths[actual]
    return edgesPath


def bfs(graph, origin, destination):
    marked = Set([origin])
    queue = deque([origin])
    paths = {}
    
    found = False
    while not found:
        actual = queue.popleft()
        unmarkedAdjacents = filter(lambda x, m=marked: x not in m, graph.adyacentes(actual))
        if destination in unmarkedAdjacents:
            paths[destination] = actual
            found = True
        else:
            for node in unmarkedAdjacents:
                paths[node] = actual
                queue.append(node)
                marked.add(node)

    return pathTo(destination, paths)

    

   
