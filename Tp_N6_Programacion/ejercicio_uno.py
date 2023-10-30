num = 1


numeros_list = []

while(num != 0):
    num = int(input("Ingrese un numero: "))
    
    if (num != 0):
        numeros_list.append(num)
    else:
        break

print("Los numeros en la lista son : ")
for numeros in numeros_list:
    print(numeros)