#!/usr/bin/python

#
# Este script prueba que los algoritmos estadisticos de orden k 
# implementados (fuerza bruta) funcionan correctamente devolviendo
# el minimo K esimo elemento de un conjunto
#

from k_selecciones import k_selecciones
from fuerza_bruta import fuerza_bruta
from ordenar_seleccionar import ordenar_seleccionar
from quick_select import quick_select
from k_heap_sort import k_heap_sort
from heap_select import heap_select

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

	def test_dado_un_conjunto_quickselect_devuelve_el_k_elem_mas_chico(self):
		self.assertEqual(quick_select(conjunto,0,len(conjunto) - 1,k),22)

	def test_dado_un_conjunto_k_heap_sort_devuelve_el_k_elem_mas_chico(self):
		self.assertEqual(k_heap_sort(conjunto, k), 22)

	def test_dado_un_conjunto_k_heap_select_devuelve_el_k_elem_mas_chico(self):
		self.assertEqual(heap_select(conjunto, k), 22)


if __name__ == '__main__':
    unittest.main()
