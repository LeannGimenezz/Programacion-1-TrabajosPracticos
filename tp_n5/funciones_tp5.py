import math
def valido_dni(dni):
    dni=str(dni)
    if(len(dni)==7 or len(dni)==8):
        return True
    else:
        return False
    
    
def longitud_ultima_palabra(string):
    string=string.split(" ")
    if(string[-1].isalpha()):
       print(len(string[-1]))
    else:
        print(len(string[-1-1]))

def verificador():   
    while True:
        full_name=input("Ingrese su nombre completo, o vacio para finalizar: ")
        if not full_name:
            break
        
        dni=input("Ingrese su numero de dni: ")
        
        while(len(dni)!=7 and len(dni)!=8):
            dni=input("Ingrese su numero de dni: ")
            
        full_name=full_name.split(" ")
        first_name=full_name[0]
        last_name=full_name[-1]
        
        numbers_dni=dni[0:3]
        identifier=first_name + str(len(last_name)) + str(numbers_dni)
        
        print(f"Su identificador es {identifier}")
        
        
def multiplos(number1, number2):
    if(number1%number2==0):
        return True
    else:
        return False
    
def temperatura(min_temp, max_temp):
    return (min_temp+max_temp)/2

def separar_con_espacio(frase):
    frase_completa =""
    for i  in range (len(frase)):
        if(frase[i].isalpha()):
            frase_completa += frase[i] + " "
        else:
            frase_completa+=frase[i]
    return frase_completa
        
def min_max(array):
    max=array[0]
    min=array[0]
    for i in array:
        if(i>max):
            max=i
        elif(i<min):
            min=i
            
    return f"El minimo es {min} y el maximo es {max}"

def area_perimetro(radio):
    area=math.pi * math.pow(radio,2)
    perimetro = 2 * math.pi * radio
    
    return f"El area de la circunferencia es {area} y el perimetro {perimetro}"

def cuenta_ocurrencias(num, digit):
    num=str(num)
    num=list(num)
    counter=0
    
    for i in num:
       i=int(i)
       if(i==digit):
           counter+=1
    return f"La cantidad de veces que se encuentra el {digit} es {counter}"


def sumDigits(number):
    add=0
    while number!=0:
        resto=number%10
        number//=10
        add+=resto

    return add

def desc_precio(carrito):

    precio = carrito['precio']
    descuento = carrito['descuento']
    total = precio - (precio * descuento / 100)

    return total

def aplicar_funcion_a_lista(funcion, lista):
    return [funcion(elemento) for elemento in lista]

def frase_a_diccionario(frase):
    palabras = frase.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

def modulo_vector(vector):
    return math.sqrt(sum([x*2 for x in vector]))

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def separar_con_espacio(frase):
    frase_completa =""
    for i  in range (len(frase)):
        frase_completa += frase[i] + " "
    return frase_completa

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def login(user, password):
    if(user=="usuario1" and password=="asdasd"):
        print("Entrando...")
        return True
    else:
        print(f"Los datos ingresados son incorrectos")
        return False