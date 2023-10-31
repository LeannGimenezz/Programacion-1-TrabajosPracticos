def digitos(num):
    if num < 10:
        return 1
    else:
        return 1 + digitos(num // 10)


def posiciones_de(a, b):
    if len(a) < len(b):
        return []
    elif a[:len(b)] == b:
        return [0] + [x + len(b) for x in posiciones_de(a[len(b):], b)]
    else:
        return [x + 1 for x in posiciones_de(a[1:], b)]
    
def is_power(n, b):
    if n == 1:
        return True
    elif n % b != 0 or n == 0:
        return False
    else:
        return is_power(n / b, b)
    
def par(n):
    if n == 1:
        return False
    else:
        return impar(n - 1)

def impar(n):
    if n == 1:
        return True
    else:
        return par(n - 1)
