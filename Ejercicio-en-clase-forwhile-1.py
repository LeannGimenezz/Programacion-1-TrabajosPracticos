#Ejercicio for

#Variable para almacenar las palabras
oficiales_lista = []
lista_mensajes=[]

# Rellenar la lista
for i  in range (5):
    oficiales_lista.append(input("Ingrese la palabra: ").lower())


user_corrimiento = int(input("Ingrese el corrimiento que utilizara el encriptamiento: "))

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","ñ","o", "p", "q", "r", "s", "t", "u", "v"," w", "x", "y","z"]

#Dos iteraciones for, una para recorrer cada elemento de la lista y el otro itera cada letra de la palabra almacenada en la lista
for i in range(len(oficiales_lista)):
    palabra = ""
    for j in range (len(oficiales_lista[i])):
        #Verifica que el valor sea una letra
        if oficiales_lista[i][j].isalpha():
            
            pos = abecedario.index(oficiales_lista[i][j])
            
            palabra+=abecedario[(pos+user_corrimiento)%27]
        else:
            palabra+=oficiales_lista[i][j]  
             
    lista_mensajes.append(palabra)
    
print(lista_mensajes)

#Ejercicio while

#Declaro variables
validador = True
pares = 0
impares = 0

#Mientras validador True pide un numero mayor a 0, si numero es 0 validador se vuelve Falso y sale del bucle
while validador==True:
    num = int(input("Defina un numero, ponga 0 si quiere salir: "))
    if num == 0 :
        validador = False
        continue
    elif num<0:
        print("Debe ingresar un numero mayor a 0")
        continue
    else:
        if num%2==0:
            pares+=1
            continue
        else:
            impares+=1
            continue
        
print(f"Los numeros pares son {pares}")
print(f"Los numeros impares son {impares}")


