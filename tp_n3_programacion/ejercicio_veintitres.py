
total = 0

while True:
    monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
    if monto == 0:
        break
    elif monto < 0:
        print("Monto inválido. Ingrese un valor positivo.")
        continue
    else:
        total += monto
        
print("El total a pagar es:", total)
