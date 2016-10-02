""" Dado un conjunto y un indice k, devuelve el k elemento mas chico
	Si k es mas grande que el tamanio del conjunto devuelve None.
"""
def ordenar_seleccionar(conjunto, k):
	if len(conjunto) < k:
		return None
		
	return sorted(conjunto)[k - 1]

