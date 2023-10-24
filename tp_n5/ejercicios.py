
from funciones_tp5 import *

#PARA DESCOMENTAR SELECCIONAR EL EJERCICIO Y PRESIONAR CTRL+K+C :D



#Ejercicio 1

#valido_dni(43637501)

#Ejercicio 2

#longitud_ultima_palabra("Hola amigos como estan")

#Ejercicio 3

#verificador()

#Ejercicio 4

#print("Defina dos numeros para evaluar si son multiplos")
#first_num=int(input("Defina el primer numero entero: "))
#second_num=int(input("Defina el segundo numero entero: "))

#multiplos(first_num, second_num)

#Ejercicio 5

#dias=int(input("Ingrese la cantidad de dias a calcular su temperatura media: "))
#for x in range(dias):
   # min_temp=int(input("Defina la temperatura minima del dia: "))
   # max_temp=int(input("Defina la temperatura maxima del dia: "))

   # print(temperatura(min_temp, max_temp))


#Ejercicio 6

#separar_con_espacio("Hola, tu")

#Ejercicio 7

#cantidad=int(input("Ingrese la cantidad de numeros que quiere ingresar: "))
#array=[]
#for i in range(cantidad):
    #numero=int(input("Ingrese un numero: "))
    #array.append(numero)
    
#print(min_max(array))


#Ejercicio 8

#radio=int(input("Defina el radio de la circunferencia: "))

#print(area_perimetro(radio))

#Ejercicio 9

#user=input("Defina su usuario: ")
#password=input("Escriba su contraseña: ")
#intentos=0

#while(not login(user,password) and intentos<2):
#    intentos+=1
#    user=input("Defina su usuario: ")
#    password=input("Escriba su contraseña: ")

#if(intentos>2):
#    print("Se acabaron los intentos")



#Ejercicio 10

#precio = int(input("Ingrese el precio del producto: "))
#porcentaje_desc = int(input("Ingrese el procentaje de descuento: "))
#carrito = {"precio":precio,"descuento":porcentaje_desc}


#print(f"El total es de: {desc_precio(carrito)}")


#Ejercicio 11

#num = int(input("Ingrese cuantos elementos desea en su lista: "))

#for i in range (num):
#    my_list = input("Ingrese un elemento de la lista: ")
    
#res = aplicar_funcion_a_lista(len,my_list)

#print(res)

#Ejercicio 12

#frase = input("Ingrese una frase: ")

#frase_dict = frase_a_diccionario(frase)

#print(frase_dict)

#Ejercicio 13

#x = int(input("Ingrese un numero del vector: "))
#y = int((input("Ingrese otro valor: ")))

#vector = [x,y]

#print(f"El modulo de un vector es igual a: {modulo_vector(vector)}")

#Ejercicio 14

#num = int(input("Ingrese un numero: "))

#if es_primo(num):
#    print(f"El numero {num} es primo")
#else:
#    print(f"El numero {num} no es primo")

#Ejercicio 15

#numeros = []
#while True:
#        numero = int(input("Ingrese un número entero (o presione Enter para finalizar): "))
#        if numero == "":
#            break
#        numeros.append(numero)
#        print(f"El factorial de {numero} es {factorial(numero)}")

#print(f"Se leyeron {len(numeros)} números.")


#Ejercicio 16

#num=int(input("Ingrese un numero entero: "))
#digit=int(input("Ingrese un digito para ver cuantas veces se encuentra: "))

#print(cuenta_ocurrencias(num, digit))

#Ejercicio 17

# numero = int(input("Ingrese un numero primo, si no, se finaliza la ejecucion: "))
# max_number = numero
# while(es_primo(numero)):
#     print(f"La suma de sus digitos es de: {sumDigits(numero)}")
#     digit=int(input("Escriba un digito para ver cuantas veces se repite: "))
#     print(cuenta_ocurrencias(numero,digit))
#     numero=int(input("Ingrese un numero primo, si no, se finaliza la ejecucion: "))
#     if (numero > max_number):
#         max_number = numero

# print(f"El factorial del numero mas grande es: {max_number} = {factorial(max_number)}")
