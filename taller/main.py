from datos import *
from metodosOrden import *
import matplotlib.pyplot as plt
from promediar import *

lista = generarDatos(5)

'''
for elemento in lista:
    print(elemento)'''


print("Quick Sort")

lista = QuickSort(lista)

'''for elemento in lista:
    print(elemento)'''

print(f'Promedio Aprobar: {promedioA(lista)}')
print(f'Promedio Perder: {promedioP(lista)}')
print(f'Promedio Desertar: {promedioD(lista)}')