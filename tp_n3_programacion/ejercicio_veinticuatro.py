
total = 0

while True:
    monto = float(input("Ingrese el monto de la venta (0 para terminar): "))
    if monto == 0:
        break
    elif monto < 0:
        print("Monto inválido. Ingrese un valor positivo.")
        continue
    else:
        total += monto
if total > 1000:
    descuento = total * 0.1
    total -= descuento
    print("Se aplicó un descuento de:", descuento)
print("El total a pagar es:", total)
