from funciones import *

list_pasajeros = list()
pasajero = tuple()
list_destino=list()
destino = tuple()


num = 1

while(num != 0):
    mostrar_menu()
    num = int(input("Ingrese una opcion: "))

    if(num == 1):
        datos=agregar_pasajeros()
        list_pasajeros.append(datos[0:3])
        tupla_ciudades = datos[3]
        list_destino.append(tupla_ciudades)


print(list_pasajeros)
print(list_destino)