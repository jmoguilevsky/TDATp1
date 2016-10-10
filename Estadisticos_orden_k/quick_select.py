def swap(a,b):
    return b,a


def partition(list, left,right):
    """ A partir de un conjunto desordenado, elige como pivote el
    ultimo elemento del conjunto list y lo deja en la posicion
    que tendria si el conjunto estuviese ordenado de menor a mayor,
    es decir, a izquierda los elementos que son menores y a derecha
    los que son mayores y devuelve el nuevo indice del pivote
    """
    storeIndex = left
    pivotValue = list[right]

    for i in range(left,right):
        if( list[i] < pivotValue ):
            list[i],list[storeIndex] = swap(list[i] , list[storeIndex])
            storeIndex = storeIndex + 1

    list[right],list[storeIndex] = swap(list[right],list[storeIndex])
    return storeIndex



def quick_select(list,k):
    """ Dado un conjunto y un indice k devuelvo el
    k elemento mas chico.
    """
    left = 0
    right = len(list) - 1
    return select(list,left,right,k)


def select(list,left,right,k):
    """ A partir de un conjunto dado por una lista y dos
    indices, ordeno un elemento, lo pongo en la posicion
    en la que estaria si el arreglo estuviese ordenado
    devuelvo el elemento si su indice es k sino
    particiono el conjunto en dos subconjuntos y vuelvo
    a iterar sobre aquel en el cual se encuentra el
    k-esimo elemento
    """
    listRelativeK = k - 1;

    if( listRelativeK < left  or listRelativeK > right):
        print("Index wont belong to the ")
        return -1

    while True:
        if ( left == right ):
            return list[left]
        pivotIndex = partition(list,left,right)
        if listRelativeK == pivotIndex:
            return list[listRelativeK]
        else:
            if listRelativeK < pivotIndex:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1
