
def ordenar_seleccionar(conjunto, k):
	""" Dado un conjunto y un indice k, devuelve el k elemento mas chico
		Si k es mas grande que el tamanio del conjunto devuelve None.
	"""
	if len(conjunto) < k:
		return None
		
	return sorted(conjunto)[k - 1]
