from funciones import *

palabras = list()
palabra = "a"


while(palabra != "listo"):

    palabra = input("Ingrese una palabra a la lista: ").lower()
    if(palabra != "listo"):
        palabras.append(palabra)
    else:
        break


palabras = list(ordenamiento_seleccion(palabras))

print(palabras)