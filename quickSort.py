import time
import random

nombre = "datasetDesordenado.txt"
file = open(nombre,"r")
aux = file.readline()
file.close()

list = [int(num) for num in aux.strip().split()]

start = time.time()

#Implementacion especifica sacada de https://stackoverflow.com/questions/18262306/quicksort-with-python
def qsort(xs, fst, lst):
# caso base
    if fst >= lst:
        return

# se inicializan los 2 punteros a los 2 extremos de la particion y se selecciona un pivote aleatorio dentro de la particion
    i, j = fst, lst
    pivot = xs[random.randint(fst, lst)]

# el puntero i busca elementos mayores al pivote a la izquierda mientras j busca elementos menores a la derecha, al encontrarse tales valores, se intercambian si los punteros aun no se intersectan.
    while i <= j:
        while xs[i] < pivot:
            i += 1
        while xs[j] > pivot:
            j -= 1

        if i <= j:
            xs[i], xs[j] = xs[j], xs[i]
            i, j = i + 1, j - 1
# cuando se intersectan los punteros las particiones estan listas y se llama recursivamente quick sort en las particiones creadas
    qsort(xs, fst, j)
    qsort(xs, i, lst)

qsort(list,0,len(list)-1)

print(str(time.time()-start) + " segundos")

aux = "quickSort"+nombre
file = open(aux,"w")
for num in list:
    file.write(str(num)+ " ")
