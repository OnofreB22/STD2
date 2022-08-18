from pandas import merge_asof
from datos import generarDatos
from metodosOrden import *
import matplotlib.pyplot as plt

import time

if __name__ == "__main__":
    cantidad = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    quick, merge, ps, bs = [],[],[],[]

    for n in cantidad:
        print(n)
        muestra = generarDatos(n)
        
        #for elemento in muestra:
        #    print(elemento)
        
        print("---[ordenado Quick]-------------------")
        inicio = time.time()
        listaQ = QuickSort(muestra)
        fin = time.time()
        quick.append(fin-inicio)
        #print(f'Metodo Quick: {(fin-inicio)} para {n} registros')

        print("---[ordenado Merge]-------------------")
        inicio = time.time()
        listaM = MergeSort(muestra)
        fin = time.time()
        merge.append(fin-inicio)
        #print(f'Metodo Merge: {(fin-inicio)} para {n} registros')

        print("---[ordenado Python Sort]-------------------")
        inicio = time.time()
        listaPS = pythonSort(muestra)
        fin = time.time()
        ps.append(fin-inicio)
        #print(f'Metodo Python Sort: {(fin-inicio)} para {n} registros')

        if n <= 1000:
            print("---[ordenado burbuja]-------------------")
            #print('---[Muestra]------')
            #for elementoX in muestra:
            #    print(elementoX)

            inicio = time.time()
            listaB = burbuja(muestra)
            fin = time.time()
            bs.append(fin-inicio)
            #print(f'Metodo Burbuja: {(fin-inicio)} para {n} registros')

        else:
            bs.append(None)

        '''
        print('---[Burbuja]------')
        for elementoX1 in listaB:
            print(elementoX1)
        print('---[Quick]------')
        for elementoX2 in listaQ:
            print(elementoX2)
        '''

    plt.plot(cantidad, quick, label ='Quick')
    plt.plot(cantidad, merge, label ='Merge')
    plt.plot(cantidad, ps, label ='PythonSort')
    plt.plot(cantidad, bs, label = 'Bubble Sort')

    plt.xlabel('Cantidad')
    plt.ylabel('Tiempo')
    
    plt.title('Algoritmos')

    plt.legend()

    plt.show()