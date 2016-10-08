def verificar(conjunto, candidato, k):
	""" Ordena el conjunto y deuvelve Verdadero
		si el indice k coincide con el del candidato
	"""
	ordenado = sorted(conjunto)
	return ordenado.index(candidato) == k - 1

def fuerza_bruta(conjunto, k):
	""" Dado un conjunto y un indice k, devuelve el k elemento mas chico.
		Si k es mas grande que el tamanio del conjunto devuelve None.
	"""
	if len(conjunto) < k:
		return None

	for candidato in conjunto:
		if verificar(conjunto, candidato, k):
			return candidato
	return None            