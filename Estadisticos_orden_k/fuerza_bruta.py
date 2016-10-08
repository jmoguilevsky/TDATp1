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


# El elemento k-esimo esta al final del conjunto
k_peor_caso = 3
cjto_peor_caso = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3]

# El elemento k-esimo esta primero en el conjunto
k_mejor_caso = 1
cjto_mejor_caso = [22, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37]
