def swap(a,b):
    return b,a


def partition(list, left,right):
    """
    """
    storeIndex = left
    pivotValue = list[right]

    for i in range(left,right):
        if( list[i] < pivotValue ):
            list[i],list[storeIndex] = swap(list[i] , list[storeIndex])
            storeIndex = storeIndex + 1

    list[right],list[storeIndex] = swap(list[right],list[storeIndex])
    return storeIndex



def quick_select(list,left,right,k):
    """
    """

    listRelativeK = k - 1;
    if ( left == right ):
        return list[left]

    pivotIndex = partition(list,left,right)

    if listRelativeK == pivotIndex:
        return list[listRelativeK]
    else:
        if listRelativeK < pivotIndex:
             return quick_select(list,left,pivotIndex - 1,k)
        else:
            return quick_select(list,pivotIndex + 1, right, k)
