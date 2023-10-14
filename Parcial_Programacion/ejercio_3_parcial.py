#Declarando variabless
user_name = input("Ingrese su nombre: ").title()
var_out = 1
user_number =1
max_numers = 0
odd_numers = 0
text_vocal = 0
vocal_numer = 0
sum_number = 0
#Mientras el numero del usuario no sea 0
while(user_number != 0):
    user_number = int(input(f"Señxr: {user_name} | Ingrese un numero | si ingresa 0 termina la ejeucion: "))

    if(user_number == 1):
        user_sum = 1
        #Mientras el numero sea distinto de 0
        while (user_sum != 0):
            user_sum = int(input(f"Señxr: {user_name} | Ingrese el numero que desee Ingresar: "))
            if (user_sum%2 == 0):
                #Si el numero es par ver cual es el mayor
                if(max_numers<user_sum):
                    max_numers = user_sum
                    
            else:
                #Si el numero es impar / calcular el promedio
                if(user_sum != 0):
                    odd_numers +=user_sum
                    sum_number += 1
        print(f"Señxr: {user_name} | El numero par mas grande es el : {max_numers}")
        if(sum_number>0):
            print(f"Señxr: {user_name} | El promedio de los numeros impares es de: {odd_numers/sum_number}")
        else:
            print(f"Señxr: {user_name} | No se ha ingresado ningun numero")
        
        
    elif(user_number == 2):
        user_text = input(f"Señxr: {user_name} | Ingrese una frase: ")
        
        #Lista que contiene vocales
        vocals = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        #Recorremos la frase y comparando cada letra con la lista de vocales y contarlas
        for lett in user_text.lower():
            if lett in vocals:
                vocals[lett] += 1
                vocal_numer +=1
        print(f"Señxr: {user_name} | Su texto tiene {vocal_numer} vocales") 
    elif(user_number == 0):
        print(F"Señxr: {user_name} | ADIOSS")
        
    
