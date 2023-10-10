
objetivo = float(input("¿Cuánto dinero quieres ahorrar? "))

ahorrado = 0
while ahorrado < objetivo:
    cantidad = float(input("¿Cuánto dinero quieres ahorrar ahora? "))
    if cantidad > 0:
        ahorrado = ahorrado + cantidad
        print(f"Has ahorrado {ahorrado} pesos")
    else:
        print("La cantidad debe ser positiva")
print(f"¡Felicidades! Has alcanzado tu objetivo de ahorrar {objetivo} pesos")
