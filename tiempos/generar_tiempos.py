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

# Truqueta: se podria pasar esto como argumento argv[1] y llamar exec(argv[1]) mas tarde. Aguante la reflexion!
ALGORITMO = ordenar_seleccionar

LONGITUD_MUESTRA = 1000
CANT_INTERVALOS = 10
TAMANIO_MUESTRA = 20


def generarListasRandom(n):
    muestras = []
    for i in range(n):
        muestra = []
        for j in range(LONGITUD_MUESTRA):
            muestra.append(int(random.random()*1e15))   # Cuando mas grande el rango del random menos chance de que salgan repetidos
        muestras.append(muestra)
    return muestras

def calcularTiempo(muestras, k):
    i = 0
    cantMuestras = len(muestras)
    tiempoTotal = 0
    for muestra in muestras:
        sys.stdout.write("\r  {}%  ".format(int(i*100.0/cantMuestras))); sys.stdout.flush()
        start = time.time()
        ALGORITMO(muestra, k)
        tiempoTotal += time.time() - start
        i += 1
    print("\r  100%  ")
    return tiempoTotal / len(muestras)



def main():
    nombreAlgoritmo = 'algoritmo_' + str(ALGORITMO).split()[1]
    output = open(nombreAlgoritmo + '.tsv', 'w')

    muestras = generarListasRandom(TAMANIO_MUESTRA)
    intervalos = [LONGITUD_MUESTRA*i/CANT_INTERVALOS for i in range(CANT_INTERVALOS)]
    resultados = []
    for k in intervalos:
        print "k = {}".format(k)
        valorMuestra = k, calcularTiempo(muestras, k)
        resultados.append(valorMuestra)

    output.write('k\ttiempo\n')
    for valor in resultados:
        output.write('{}\t{}\n'.format(valor[0], valor[1]))

    plotter.plotResults(resultados)
    plotter.showResults()



if __name__ == "__main__":
    main()
