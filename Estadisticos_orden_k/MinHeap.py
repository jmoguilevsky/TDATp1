""" """
class MinHeap:

	def __init__(self):
		self.elementos = []

	""" """
	def encolar(self, elem):
		self.elementos.append(elem)
		self.__upheap__(len(self.elementos) - 1)

	""" """
	def desencolar(self):
		tamHeap = len(self.elementos)
		if tamHeap <= 0:
			return None

		primerElem = self.elementos[0]
		self.elementos[0] = self.elementos[tamHeap - 1]
		self.elementos.pop(tamHeap - 1)
		self.__downheap__(0)
		return primerElem

	""" """
	def __upheap__(self, pos_hijo):
		if pos_hijo == 0: return
		pos_padre = self.__buscar_padre__(pos_hijo)
		if self.elementos[pos_hijo] < self.elementos[pos_padre]:
			self.__swap__(pos_hijo, pos_padre)
			self.__upheap__(pos_padre)

	""" """
	def __downheap__(self, pos_padre):
		if pos_padre >= len(self.elementos): return
		pos_hijo = self.__buscar_hijo_menor__(pos_padre)
		if pos_hijo > -1:
			if self.elementos[pos_hijo] < self.elementos[pos_padre]:
				self.__swap__(pos_hijo, pos_padre)
				self.__downheap__(pos_hijo)

	""" """
	def __buscar_padre__(self, pos):
		if pos % 2 == 0: return pos/2 -1
		return pos/2

	""" """
	def __buscar_hijo_menor__(self, pos_padre):
		pos_hijo_1 = (2*pos_padre)+1
		pos_hijo_2 = (2*pos_padre)+2

		if (pos_hijo_1 >= len(self.elementos)): return -1			#No tiene hijos
		if (pos_hijo_2 >= len(self.elementos)): return pos_hijo_1 	#Tiene 1 solo hijo
		if self.elementos[pos_hijo_1] < self.elementos[pos_hijo_2]:
			return pos_hijo_1
		return pos_hijo_2

	""" """
	def __swap__(self, posi, posj):
		swap = self.elementos[posi]
		self.elementos[posi] = self.elementos[posj]
		self.elementos[posj] = swap