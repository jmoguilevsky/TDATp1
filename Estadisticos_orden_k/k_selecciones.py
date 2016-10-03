""" Dado un conjunto y un indice k, devuelve el k elemento mas chico
	Si k es mas grande que el tamanio del conjunto devuelve None.
"""
def k_selecciones(conjunto, k):
	tamConjunto = len(conjunto)
	if tamConjunto < k: 
		return None

	for i in xrange(k):
		minElem = conjunto[i]
		minPos = i
		for pos in xrange(i, tamConjunto):
			if conjunto[pos] < minElem:
				minElem = conjunto[pos]
				minPos = pos
		#swap
		conjunto[minPos] = conjunto[i]
		conjunto[i] = minElem

	return conjunto[k - 1]