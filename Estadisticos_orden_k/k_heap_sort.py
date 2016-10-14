from Heap import MinHeap

def k_heap_sort(conjunto, k):
	""" Dado un conjunto y un indice k, devuelve el k elemento mas chico.
		Si k es mas grande que el tamanio del conjunto devuelve None.
	"""
	heap = MinHeap()
	heap.heapify(conjunto)

	for i in xrange(k - 1):
		heap.sacar_primero()
	return heap.sacar_primero()
