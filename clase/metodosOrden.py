#=========================================================
def QuickSort(datos):
    if len(datos) <= 1:
        return datos   
    pivote = datos[len(datos)//2]
    izq = [x for x in datos if x < pivote]
    centro = [x for x in datos if x == pivote]
    der = [x for x in datos if x > pivote]
    return QuickSort(izq) + centro + QuickSort(der)
#========================================================
def burbuja(lista):
    for i in range(len(lista)): 
        for j in range(len(lista)):
            if lista[i]<lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    return lista
#=======================================================

def MergeSort(datos):
    if len(datos) <= 1:
        return datos
    if len(datos) == 2:
        return sorted(datos)
    mitad = len(datos) // 2
    return op_Merge(MergeSort(datos[:mitad]),MergeSort(datos[mitad:]))

def op_Merge(datosX, datosY):
    indA = indB = 0
    out = []
    while indA < len(datosX) and indB < len(datosY):
        if datosX[indA] < datosY[indB]:
            out.append(datosX[indA])
            indA += 1
        else:
            out.append(datosY[indB])
            indB += 1
    out += datosX[indA:] + datosY[indB:]
    return out


def pythonSort(datos):
    return sorted(datos)
