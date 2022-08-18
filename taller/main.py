from datos import *
from metodosOrden import *

lista = generarDatos(5)

for elemento in lista:
    print(elemento)

print("Quick Sort")

lista = QuickSort(lista)

for elemento in lista:
    print(elemento)