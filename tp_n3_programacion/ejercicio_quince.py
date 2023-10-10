user_number = -1
while(user_number<=0):
    user_number = int(input("Ingrese un numero mayor que cero: "))
    if user_number<=0:
        print("Vuelva a ingresar el valor")
    else:
        for i in range(1,user_number+1):
            if(user_number%i == 0):
                print(i)
