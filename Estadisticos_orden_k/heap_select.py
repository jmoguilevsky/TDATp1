from Heap import MaxHeap

def heap_select(conjunto, k):
	""" Dado un conjunto y un indice k, devuelve el k elemento mas chico.
		Si k es mas grande que el tamanio del conjunto devuelve None.
	"""
	if len(conjunto) < k:
		return None

	heap = MaxHeap()
	for i in xrange(k):
		heap.ingresar(conjunto[i])
	for j in xrange(k, len(conjunto)):
		if conjunto[j] < heap.obtener_primero():
			heap.sacar_primero()
			heap.ingresar(conjunto[j])
	return heap.sacar_primero()