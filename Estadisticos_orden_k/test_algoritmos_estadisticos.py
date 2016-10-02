#!/usr/bin/python
from k_selecciones import k_selecciones
from fuerza_bruta import fuerza_bruta
from ordenar_seleccionar import ordenar_seleccionar
from k_heap_select import k_heap_select
from MinHeap import MinHeap

import unittest

conjunto = [1,6,9,3,5,10,3,12,15,60,0,9,4,41,22,16]
k = 14

class TestEstadisticoClass(unittest.TestCase):
	
	def test_dado_un_conjunto_k_selecciones_devuelve_el_k_elem_mas_chico(self):
		self.assertEqual(k_selecciones(conjunto, k), 22)

	def test_dado_un_conjunto_fuerza_bruta_devuelve_el_k_elem_mas_chico(self):
		self.assertEqual(fuerza_bruta(conjunto, k), 22)

	def test_dado_un_conjunto_ordenar_seleccionar_devuelve_el_k_elem_mas_chico(self):
		self.assertEqual(ordenar_seleccionar(conjunto, k), 22)

	def test_dado_un_conjunto_k_heap_select_devuelve_el_k_elem_mas_chico(self):
		heap = MinHeap()
		for elem in conjunto:
			heap.encolar(elem)
		self.assertEqual(k_heap_select(heap, k), 22)
		
if __name__ == '__main__':
    unittest.main()

