suma = 0
pares = 0
user_number = int(input("Ingrese un numero: "))
while(user_number != -1):
    suma += user_number
    if(user_number%2 == 0):
        pares +=1
    print(f"El resultado de la suma es de: {suma}")
    user_number = int(input("Ingrese un numero: "))
print(f"La cantidad de numero pares es de: {pares}")    