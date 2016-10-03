from MinHeap import MinHeap

def k_heap_select(heap, k):
	for i in xrange(k - 1):
		heap.desencolar()
	return heap.desencolar()
