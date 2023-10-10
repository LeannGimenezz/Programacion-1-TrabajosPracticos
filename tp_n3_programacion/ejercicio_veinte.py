suma = 0

user_number = int(input("Ingrse un numero: "))

while(user_number != 0):
    suma +=user_number
    user_number = int(input("Ingrese otro numero: "))
    
print(f"La suma total es de: {suma}")