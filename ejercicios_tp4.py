#ejercicio a

"""
x = 0
while x in range(31):
    if(x==15):
        print("X vale 15 el bucle finaliza")
        break
    elif(x==4 or x==6 or x==10):
        print(f"The value {x} of x was skipped")
        x +=1
    else:
        print(f"The value of the loop is {x}")
        x += 1
"""
        
#ejercicio b
""""
line=input("Escriba una linea de texto para transformarla a mayuscula: ")

while len(line)>0:
    print(line.upper())
    line=input("Escriba una linea de texto para transformarla a mayuscula: ")
"""    
    
#ejercicio c
""""
operacion = input("Escriba su operacion con D/R (deposito/retiro) y el monto deseado de la operacion: ")
suma = 0
while len(operacion)>0:
    if(operacion[0].lower()=="d"):
        suma = suma + int(operacion[2:len(operacion)])
        print(suma)
        operacion = input("Escriba su operacion con D/R (deposito/retiro) y el monto deseado de la operacion: ")
    elif (operacion[0].lower()=="r"):
        suma = suma - int(operacion[2:len(operacion)])
        print(suma)
        operacion = input("Escriba su operacion con D/R (deposito/retiro) y el monto deseado de la operacion: ")
    else:
        print("Error al introducir la operacion, intente de nuevo")
        operacion = input("Escriba su operacion con D/R (deposito/retiro) y el monto deseado de la operacion: ")
        
print(f"El valor final es de {suma}")

"""
#ejercicio d
""""
num = int(input("Defina un numero mayor que 1: "))
primos = 0

def es_primo(num):
    divisores = 0
    for x in range(num, 0, -1):
        if(num%x==0):
            divisores+=1

    if(divisores==2):
        return True
    
    
while num>1:
    if(es_primo(num)):
        primos +=1
        print(num)
        num = int(input("Defina un numero mayor que 1: "))
    else:
        print(num)
        num = int(input("Defina un numero mayor que 1: "))

    
print(f"La cantidad total de numeros primos ingresados fue {primos}")
"""

#ejercicio e
""""
first_year=int(input("Ingrese el primer año: "))
second_year=int(input("Ingrese el segundo año: "))

def es_bisiesto(year):
    if(year%400==0):
        return True
    elif(year%4==0 and year%100!=0):
        return True
    else:
        return False

    

if(first_year>second_year):
    for x in range(second_year, first_year, 1):
        if(x%10==0 and es_bisiesto(x)):
            print(x)
else:
    for x in range(first_year, second_year, 1):
        if(x%10==0 and es_bisiesto(x)):
            print(x)         
"""

#ejercicio f

""""
for x in range(1, 21):
    if(x%2==0):
        print(x)
    else:
        continue 
        
"""
    
#ejercicio g
""""
lista = [1, 3, 5, 6, 8, 10, 12]
num = int(input("Defina un numero para buscar en la lista: "))

for elem in lista:
    if(elem==num):
        print("Numero encontrado")
        break
    else:
        continue
"""

#ejercicio h

opciones=int(input("Defina el menu de las siguientes opciones, marque 0 si quiere salir: "))

while opciones != 0:
    opciones=int(input("Defina el menu de las siguientes opciones, marque 0 si quiere salir: "))
    if(opciones==0):
        break
