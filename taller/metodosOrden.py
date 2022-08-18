def QuickSort(datos):
    if len(datos) <= 1:
        return datos   
    pivote = datos[len(datos)//2]
    izq = [x for x in datos if x < pivote]
    centro = [x for x in datos if x == pivote]
    der = [x for x in datos if x > pivote]
    return QuickSort(izq) + centro + QuickSort(der)