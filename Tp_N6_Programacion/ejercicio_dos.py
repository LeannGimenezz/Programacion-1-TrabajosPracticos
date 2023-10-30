

list_numeros = [1,2,23,12,10,4,6,8,9,15]

num_eliminar = int(input("Ingrese el numero que desea eliminar: "))

if (num_eliminar in list_numeros):
    list_numeros.remove(num_eliminar)
    print(f"Perfecto el numero: {num_eliminar} ha sido eliminado de la lista")
    print(list_numeros)
else:
    print(f"No se ha encontrado el valor: {num_eliminar}")

