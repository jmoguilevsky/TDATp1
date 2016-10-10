#!/usr/bin/python

#
# Este script genera los datos de los tiempos de un algoritmo dado.
# Cambiar el algoritmo con la variable ALGORITMO. Recordar importar el archivo!
#

import random
import time
import sys; sys.path.insert(0, '..')
import plotter

from fuerza_bruta import fuerza_bruta
from ordenar_seleccionar import ordenar_seleccionar
from heap_select import heap_select
from k_heap_sort import k_heap_sort
from k_selecciones import k_selecciones
from quick_select import quick_select

LONGITUD_MUESTRA = 500
CANT_INTERVALOS = 10
TAMANIO_MUESTRA = 200


def generarListasRandom(n):
    """ A partir de un numero n, genera un lista de n muestras random,
        cada una de LONGITUD_MUESTRA elementos
    """
    muestras = []
    for i in range(n):
        muestra = []
        for j in range(LONGITUD_MUESTRA):
            muestra.append(int(random.random()*1e15))   # Cuando mas grande el rango del random menos chance de que salgan repetidos
        muestras.append(muestra)
    return muestras

def calcularTiempo(algoritmo, muestras, k):
    """ Dado un algoritmo y un conjunto de muestras, calcula el tiempo que le lleva
        al algoritmo ejecutar cada muestra y devuelve el promedio del tiempo total
        sobre la cantidad de muestras
    """
    i = 0
    cantMuestras = len(muestras)
    tiempoTotal = 0
    for muestra in muestras:
        sys.stdout.write("\r  {}%  ".format(int(i*100.0/cantMuestras))); sys.stdout.flush()
        start = time.time()
        eval(algoritmo)(muestra, k)
        tiempoTotal += time.time() - start
        i += 1
    print("\r  100%  ")
    return tiempoTotal / len(muestras)



def main(algoritmo):
    """ Genera una lista de muestras random y calcula los resultados de
        ejecutar las muestras con distinto valor de K para un algoritmo
        pasado por parametro.
        Luego dibuja los resultados obtenidos
    """
    nombreAlgoritmo = 'algoritmo_' + algoritmo
    output = open(nombreAlgoritmo + '.tsv', 'w')

    muestras = generarListasRandom(TAMANIO_MUESTRA)
    intervalos = [LONGITUD_MUESTRA*i/CANT_INTERVALOS for i in range(CANT_INTERVALOS)]
    resultados = []
    for k in intervalos:
        k += 1
        print "k = {}".format(k)
        valorMuestra = k, calcularTiempo(algoritmo, muestras, k)
        resultados.append(valorMuestra)

    output.write('k\ttiempo\n')
    for valor in resultados:
        output.write('{}\t{}\n'.format(valor[0], valor[1]))

    plotter.plotResults(resultados)
    plotter.showResults()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Se debe ingresar como unico argumento el nombre del algoritmo')
    sys.exit(main(sys.argv[1]))
