from datos import *
from metodosOrden import *
import matplotlib.pyplot as plt

lista = generarDatos(100000)
'''
for elemento in lista:
    print(elemento)

print("Quick Sort")'''

lista = QuickSort(lista)

'''
for elemento in lista:
    print(elemento)'''

grado = ['Parvulos', 'Jardin', '1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º', '10º', '11º', 'Universidad']
nEst = [0]*14

for i in lista:
    nEst[i.edad - 5] = nEst[i.edad - 5]+1

plt.bar(grado, nEst)
plt.title('grado vs est')
plt.xlabel('Grados')
plt.ylabel('cantidad')

plt.show()