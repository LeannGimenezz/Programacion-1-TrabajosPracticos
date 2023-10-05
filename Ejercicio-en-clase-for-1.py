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
          



