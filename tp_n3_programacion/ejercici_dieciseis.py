user_numbers = int(input("Ingrese cuantos numeros quiere ingresar"))
negative_numbers = 0
for i in range(user_numbers):
    numbers = int(input("introduzca un numero: "))
    if(numbers<0):
        negative_numbers +=1
        
print(f"Se han introducido: {negative_numbers} numeros negativos")