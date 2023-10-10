def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Ingrese un número entero positivo: "))

f = factorial(n)

print(f"El factorial de {n} es {f}")
