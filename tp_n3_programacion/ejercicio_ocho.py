
user_num = int(input("Ingrese un numero entero: "))

for i in range(user_num):
    aux_num = 1
    for j in range(i+1):
        print(aux_num,end=" ")
        aux_num +=2
        
    print("")
    
