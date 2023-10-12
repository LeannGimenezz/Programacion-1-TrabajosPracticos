import random
#Declaro las palabras
list_ahorcado = ["pelota","tomate", "futbol", "amarillo", "beisbol", "bicicleta", "tenis", "jarra", "cuchara", "tenedor"]
palabra = ""
#Numero entre el rango establecido
"""
num = int(input("Elija un numero para seleccionar una palabra al azar entre 1 y 10: "))
while(num < 1 or num > 10):
    num = int(input("Recuerde que el numer tiene que ser entre 1 y 10: "))
"""
#Asigna y convierte a lista
#palabra_seleccionada=list(list_ahorcado[num-1])
palabra_seleccionada=random.choice(list_ahorcado)
#Establecemos las vidas
lives_left=6
#Rellenar palabra
for x in range(len(palabra_seleccionada)):
    palabra += "_"

palabra = list(palabra)
print(palabra)

contador =0 
#Mientras tenga vidas y no haya completado la palabra entra al bucle
while(lives_left>0 and contador < len(palabra_seleccionada)):
    #Pedir al usuario la palabra
    letra_seleccionada= input("Ingrese una letra para buscar: ").lower()
    if(len(letra_seleccionada)==1):
        #La letra tiene que estar en la palabra
        if(letra_seleccionada in palabra_seleccionada):
            #Si la letra ingresada no se repite con una ya ingresada anteriormente entra
            if(letra_seleccionada not in palabra):
                print("Correcto")
                for i in range (len(palabra_seleccionada)):
                    if (letra_seleccionada == palabra_seleccionada[i]):
                        palabra[i] = letra_seleccionada
                        print(palabra)
                        contador+=1
                        continue
            else:
                print("La letra ya fue ingresada")
                lives_left = lives_left - 1
                print(lives_left)
            
        else:
            print("Letra incorrecta")
            lives_left=lives_left-1
            print(f"Vidas restantes {lives_left}")
    else:
        print("Error al ingresar la letra")
        continue
#Si queda sin vidas muestra un mensaje de derrota, si no de victoria
if(lives_left == 0):
    print(f"Perdiste, la palabra era {palabra_seleccionada}")
else:
    print("Felicidades, ganaste maquina")
    