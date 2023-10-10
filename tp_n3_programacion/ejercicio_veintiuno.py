user_number = int(input("Ingrese un numero: "))
mayor = user_number

while(user_number != 0):
    if(user_number>mayor):
        mayor = user_number
        
    user_number = int(input("Ingrese otro numero: "))

print(f"El numero mayor es: {mayor}")