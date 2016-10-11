from abc import abstractmethod

class Heap:
	""" Clase abstracta que representa un Heap (conjunto de elementos ordenados
		donde el primer elemento representa el primer elemento ordenado), 
		En el mismo se puede encolar, desencolar elementos y obtener su primer 
		elemento.
		Para definir el tipo de Heap, debe redefinir el metodo
		abstracto 'comparar_posiciones'
	"""

	def __init__(self):
		""" Inicializa un vector de elementos 
		"""
		self.elementos = []

	def heapify(self, elementos):
		""" A partir de un conjunto de elementos, se lo convierte en un Heap
		"""
		self.elementos = elementos
		pos_inicial = (len(elementos) - 2) / 2
		while pos_inicial >= 0:
			self.__downheap__(pos_inicial)
			pos_inicial -= 1


	def ingresar(self, elem):
		""" INgresa un elemento al final del vector de elementos.
			Luego aplica el metodo upheap para ubicarlo en la 
			posicion correspondiente del Heap 
		"""
		self.elementos.append(elem)
		self.__upheap__(len(self.elementos) - 1)

	def sacar_primero(self):
		""" Saca al primer elemento y lo devuelve.
			Luego aplica el metodo downheap sobre el ultimo elemento 
			para ubicarlo en la posicion correspondiente y que el
			Heap quede armado nuevamente. 
		"""
		tamHeap = len(self.elementos)
		if tamHeap <= 0:
			return None

		primerElem = self.elementos[0]
		self.elementos[0] = self.elementos[tamHeap - 1]
		self.elementos.pop(tamHeap - 1)
		self.__downheap__(0)
		return primerElem

	def obtener_primero(self):
		""" Devuelve el primero elemento del Heap
		"""
		if len(self.elementos) <= 0:
			return None
		return self.elementos[0]

	def __upheap__(self, pos_hijo):
		""" Dada una posicion, busca la posicion del padre y en
			caso que la comparacion entre el hijo y el padre sea
			verdadera, cambia de posicion a los elementos y vuelve
			a llamar al metodo de UpHeap
		"""
		if pos_hijo == 0: return
		pos_padre = self.__buscar_padre__(pos_hijo)
		if self.__comparar_posiciones__(pos_hijo, pos_padre):
			self.__swap__(pos_hijo, pos_padre)
			self.__upheap__(pos_padre)

	def __downheap__(self, pos_padre):
		""" Dada una posicion de padre, busca la posicion del hijo
			menor y si existe y la comparacion entre el hijo y el 
			padre es verdadera, cambia de posicion a los elementos 
			y vuelve a llamar al metodo de DownHeap
		"""
		if pos_padre >= len(self.elementos): return
		pos_hijo = self.__buscar_hijo_menor__(pos_padre)
		if pos_hijo > -1:
			if self.__comparar_posiciones__(pos_hijo, pos_padre):
				self.__swap__(pos_hijo, pos_padre)
				self.__downheap__(pos_hijo)

	def __buscar_padre__(self, pos):
		""" Dada una posicion, devuelve la posicion de su padre
		"""
		if pos % 2 == 0: return pos/2 -1
		return pos/2

	def __buscar_hijo_menor__(self, pos_padre):
		""" Dada la posicion de un padre, devuelve la posicion de 
			su hijo menor.
		"""
		pos_hijo_1 = (2*pos_padre)+1
		pos_hijo_2 = (2*pos_padre)+2

		if (pos_hijo_1 >= len(self.elementos)): return -1			#No tiene hijos
		if (pos_hijo_2 >= len(self.elementos)): return pos_hijo_1 	#Tiene 1 solo hijo
		if self.__comparar_posiciones__(pos_hijo_1, pos_hijo_2):
			return pos_hijo_1
		return pos_hijo_2

	def __swap__(self, posi, posj):
		""" Cambia los elementos entre la posicion posi y la posicion posj
		"""
		swap = self.elementos[posi]
		self.elementos[posi] = self.elementos[posj]
		self.elementos[posj] = swap

	@abstractmethod
	def __comparar_posiciones__(self, posi, posj):
		""" Compara los elementos de las posiciones posi y posj y
			Devuelve True o False segun el tipo de comparacion que
			se realice.
		"""
		return NotImplemented


class MaxHeap(Heap):
	""" La clase representa un Heap de Maximo, donde el primer elemento
		sera el maximo del conjunto.
	"""

	def __comparar_posiciones__(self, posi, posj):
		""" Compara los elementos de las posiciones posi y posj y
			Devuelve True si el elemento de la posicion posj es menor
			que el de la posicion posi
		"""
		if self.elementos[posi] > self.elementos[posj]:
			return True
		return False

class MinHeap(Heap):
	""" La clase representa un Heap de Minimo, donde el primer elemento
		sera el minimo del conjunto.
	"""

	def __comparar_posiciones__(self, posi, posj):
		""" Compara los elementos de las posiciones posi y posj y
			Devuelve True si el elemento de la posicion posi es menor
			que el de la posicion posj
		"""
		if self.elementos[posi] < self.elementos[posj]:
			return True
		return False
