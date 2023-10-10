number = int(input("Ingrese cuantos numero quiere comprobar: "))

for i in range(number):
    user_number = int(input("Ingrese el numero "))
    if(user_number % 2 == 0):
        print("Es par")
    else:
        print("Es impar")  
    