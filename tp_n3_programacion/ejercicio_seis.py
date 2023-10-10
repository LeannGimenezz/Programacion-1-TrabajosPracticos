user_num = int(input("Ingrese un numero entero: "))

for i in range(1,user_num+1):
    for j in range(i):
        print("*",end="")
    print("")