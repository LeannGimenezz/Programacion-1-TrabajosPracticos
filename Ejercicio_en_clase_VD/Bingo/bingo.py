import random
from funciones_bingo import *
#carton=list()

carton=[[1,2,3],[4,5,6],[7,8,9]]
counter=0



# for i in range(5):
#     carton.append([])
#     for j in range(5):
#         while j < 26: 
#             print(i, j)
#             num=int(input("Ingrese un numero del 1 al 75: "))
#             booleano= recorrer_carton(num, carton)
#             print(booleano)
#             if (booleano and num>0 and num<76):
#                 carton[i].append(num)
#                 break
#             elif(not booleano):
#                 print("El numero ya se encuentra en el carton")
                
#             else:
#                 print("error al ingresar el numero intente denuevo")



opc="si"

while opc=="si":
    bola=random.randint(1,75)
    print(bola)
    bola_eliminada=eliminar_numero(bola,carton)
    opc=input("Desea tirar otra bola? (si/no): ").lower()
    completa_col(bola_eliminada, carton)

    
    
for i in range(len(carton)):
    if(len(carton[i])==0):
        print("Terminaste una linea felicidades!!!!")
        break



          
print(carton)

