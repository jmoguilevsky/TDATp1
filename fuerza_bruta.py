def verificar(conjunto, candidato, k):
    ordenado = sorted(conjunto)
    return ordenado.index(candidato) == k - 1

""" Dado un conjunto y un indice k, devuelve el k elemento mas chico
	Si k es mas grande que el tamanio del conjunto devuelve None.
"""
def fuerza_bruta(conjunto, k):
    for candidato in conjunto:
        if verificar(conjunto, candidato, k):
            return candidato
    return None            
