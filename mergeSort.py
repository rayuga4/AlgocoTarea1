import time

nombre = "datasetDesordenado.txt"
file = open(nombre,"r")
aux = file.readline()
file.close()

list = [int(num) for num in aux.strip().split()]

start = time.time()

#Implementacion especifica sacada de https://www.geeksforgeeks.org/merge-sort/
def merge(arr,izq,medio,der):
# se obtenien los tamaños de las sublistas y se inicializan
    n1 = medio-izq+1
    n2 = der-medio
    auxIzq = [0]*n1
    auxDer = [0]*n2
    for i in range(n1):
        auxIzq[i] = arr[izq+i]
    for j in range(n2):
        auxDer[j] = arr[medio+1+j]
    i = j = 0
    k = izq
# se insertan en el orden correcto en la lista original el contenido de las particiones
    while i<n1 and j<n2:
        if auxIzq[i]<=auxDer[j]:
            arr[k] = auxIzq[i]
            i+=1
        else:
            arr[k] = auxDer[j]
            j+=1
        k+=1
    while i<n1:
        arr[k] = auxIzq[i]
        i+=1
        k+=1
    while j<n2:
        arr[k] = auxDer[j]
        j+=1
        k+=1

def mergeSort(arr,izq,der):
    if izq<der:
        medio = (izq+der)//2
        mergeSort(arr,izq,medio)
        mergeSort(arr,medio+1,der)
        merge(arr,izq,medio,der)

mergeSort(list,0,len(list)-1)

print(str(time.time()-start) + " segundos")

aux = "mergeSort"+nombre
file = open(aux,"w")
for num in list:
    file.write(str(num)+ " ")
