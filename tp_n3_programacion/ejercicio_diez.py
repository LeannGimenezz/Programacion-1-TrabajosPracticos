user_number = int(input("Ingrese un numero: "))

for i in range(2,user_number):
    if(user_number% i == 0):
        print("No es primo")
        break
else:
    print("Es primo")