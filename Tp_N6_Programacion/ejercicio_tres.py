num = 1
sum = 0
numeros_list = list()
while(num != 0):
    num = int(input("Ingrese numeros a la lista: "))
    if(num != 0):
        numeros_list.append(num)
        sum += num
    else:
        print("Se ha finalizado la ejecucion")
        break
    
print(f"El resultado de la suma de la lista es de: {sum}")