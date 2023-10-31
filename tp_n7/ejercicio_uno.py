from funciones import *


numeros = list()
num = 1
while(num != 0):
    num = int(input("Ingrese el valor en la lista: "))
    if(num != 0):
        numeros.append(num) 
    else:
        break

numeros = list(ordenamiento_burbuja(numeros))

print(numeros)
