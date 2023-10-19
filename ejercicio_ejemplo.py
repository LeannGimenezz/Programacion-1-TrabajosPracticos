user_number = 1
sum_total = 0
def sum_numbers(n):
    suma = 0
    while n > 0:
        digit = n % 10
        suma += digit
        n = n // 10
    return suma

while(user_number != 0):
    
    user_number = int(input("Ingrese un numero, si desea salir ingrese 0: "))
    if(user_number != 0):
        sum_total += user_number
        print(f"La suma de los digitos del numero: {user_number} es de: {sum_numbers(user_number)}")
    else:
        print("ADIOSS")

print(f"LA SUMA TOTAL DE LOS NUMEROS INGRESADOS ES DE: {sum_total}")